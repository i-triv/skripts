ps
filtered in ps
# Define the input and output file paths
$inputFile = "input.txt"
$outputFile = "result.txt"

# Read the input file content
$inputContent = Get-Content $inputFile

# The string to filter
$filterString = "not included:text"

# Filter the content based on the string
$filteredContent = $inputContent | Where-Object { $_ -match $filterString }

# Write the filtered content to the output file
$filteredContent | Set-Content $outputFile
