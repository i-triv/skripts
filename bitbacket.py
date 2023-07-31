
import requests

def get_merged_branches():
    base_url = 'https://your-bitbucket-server-url/rest/api/1.0'
    project_key = 'your_project_key'
    repo_slug = 'your_repo_slug'
    username = 'your_username'
    password = 'your_password'

    branches_url = f'{base_url}/projects/{project_key}/repos/{repo_slug}/compare/changes?from=master'
    response = requests.get(branches_url, auth=(username, password))

    if response.status_code == 200:
        merged_branches = []
        changes = response.json()['changes']
      
        for change in changes:
            to_hash = change['toHash']
            link_url = f'{base_url}/projects/{project_key}/repos/{repo_slug}/commits/{to_hash}/branches'
            branch_response = requests.get(link_url, auth=(username, password))

            if branch_response.status_code == 200:
                branch_name = branch_response.json()['values'][0]['displayId']
                merged_branches.append(branch_name)

        return merged_branches
    else:
        print(f'Response status code: {response.status_code}')
        return None

merged_branches_list = get_merged_branches()
if merged_branches_list:
    print("Merged branches:")
    for branch in merged_branches_list:
        print(branch)
else:
    print("Error occurred while fetching merged branches.")

----------------
import requests

def get_merged_branches():
    username = 'your_username'
    password = 'your_password'
    repo_slug = 'your_repository_slug'
    url = f'https://api.bitbucket.org/2.0/repositories/{username}/{repo_slug}/branches'
    response = requests.get(url, auth=(username, password))
    response_json = response.json()

    merged_branches = []
    for branch in response_json['values']:
        if branch['merge'] and branch['merge']['status'] == 'MERGED':
            merged_branches.append(branch['name'])
    
    return merged_branches

merged_branches_list = get_merged_branches()
print("Merged branches:")
for branch in merged_branches_list:
    print(branch)

import requests

def get_merged_branches():
    username = 'your_username'
    password = 'your_password'
    repo_slug = 'your_repository_slug'
    url = f'https://api.bitbucket.org/2.0/repositories/{username}/{repo_slug}/branches?pagelen=100'
    response = requests.get(url, auth=(username, password))
    response_json = response.json()

    merged_branches = []
    for branch in response_json['values']:
        branch_url = branch['links']['commits']['href']
        commit_response = requests.get(branch_url, auth=(username, password))
        commit_response_json = commit_response.json()
        last_commit = commit_response_json['values'][0]['hash']
        if last_commit == branch['target']['hash']:
            merged_branches.append(branch['name'])

    return merged_branches

merged_branches_list = get_merged_branches()
print("Merged branches:")
for branch in merged_branches_list:
    print(branch)
