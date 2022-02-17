import os.path

text = 'aabla-bla-bla'

while True:
    location = input('Please, type absolute path where you want to save it (using space brakes): ')
    # location = 'home venus Serg Coding Python_Basic Module22 04_files_and_folders'
    location = os.sep + os.sep.join(location.split())
    if os.path.exists(location) is True:
        break
    else:
        print('Oops, something went wrong.')

file = input('File name: ')

if os.path.isfile(location + os.sep + file) is True:
    responce = input('Are you sure that you want to rewrite this file? ')
    if responce == 'yes':
        file_name = open(location + os.sep + file, 'w+')
        file_name.write(text)
    else:
        print('Ok, Bro.')
else:
    file_name = open(location + os.sep + file, 'w+')
    file_name.write(text)

file_name.close()