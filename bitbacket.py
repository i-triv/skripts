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
