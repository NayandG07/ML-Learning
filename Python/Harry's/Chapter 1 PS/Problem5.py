import os

# specify the directory you want to list
directory_path = '/Windows'

# List all the files and directories in the specific path
contents = os.listdir(directory_path)

# Print each file and directory name
for items in contents:
    print(items)