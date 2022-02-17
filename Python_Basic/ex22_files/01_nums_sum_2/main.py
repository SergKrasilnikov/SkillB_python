numbers_file = open('numbers.txt', 'r')

num = 0
for i_line in numbers_file:
    i_line = i_line.strip(' ')
    i_line = i_line.strip('\n')
    if i_line.isdigit():
        num += int(i_line)

print('Содержание файла numbers.txt\n' + str(num))
numbers_file.close()