import os

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

#there are comments
files_filtered = (x for x in files('.') if x.endswith('.py'))
for file in files_filtered:
    count = 0
    with open(file, 'r') as open_file:
        lines = open_file.readlines()[::1]
        for line in lines:
            if not line.strip() == '' and not line.strip().startswith('#'):
                count += 1
        print(f'{count} lines in file {file}.')