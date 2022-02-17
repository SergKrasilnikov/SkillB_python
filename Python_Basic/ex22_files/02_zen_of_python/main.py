zen_file = open('zen.txt', 'r')

lines = zen_file.readlines()[::-1]
for line in lines:
    print(line, end='')

zen_file.close()