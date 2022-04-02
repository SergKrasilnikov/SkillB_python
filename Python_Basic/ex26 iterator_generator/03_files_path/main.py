import os

def en_files_path(files_list: list) -> list:
    for file in files_list:
        yield file

dirname = '/'
search = 'var'
files = en_files_path(os.listdir(dirname))
for item in files:
    print(os.path.join(dirname, item))
    if item == search:
        break
else:
    print(f'Did not find folder {search} in catalog {dirname}.')