import os

def getFolderSize(folder):
    total = [os.path.getsize(folder), 0, 0]
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total[2] += 1
            total[0] += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            tmp = getFolderSize(itempath)
            total[0] += tmp[0]
            total[1] += tmp[1] + 1
            total[2] += tmp[2]

    return total

# path = '/home/venus/Serg/Coding/Python_Basic/Module14'
path = input('The folder location: ')

mylist = getFolderSize(path)

print(f'Folder size: {mylist[0]/1024} kb')
print('Subfolders:', mylist[1])
print('Files in subfolders:', mylist[2])