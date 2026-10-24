import os

directory_path = '/Windows'

contents = os.listdir(directory_path)

for items in contents:
    print(items)