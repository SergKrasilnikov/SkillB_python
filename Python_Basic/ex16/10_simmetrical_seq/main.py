def palindrome(num_list):
    reversed_list = []
    for num_loop in range(len(num_list) - 1, -1, -1):
        reversed_list.append(num_list[num_loop])
    if num_list == reversed_list:
        return True
    else:
        return False


base_num = []
new_num = []
result = []

num = int(input('Кол-во чисел: '))

for num_loop in range(num):
    base_num.append(int(input('Число: ')))

for num_loop in range(0, len(base_num)):
    for num_in_loop in range(num_loop, len(base_num)):
        new_num.append(base_num[num_in_loop])
    if palindrome(new_num):
        for result_loop in range(0, num_loop):
            result.append(base_num[result_loop])
        result.reverse()
        break
    new_num = []

print('Последовательность', str(base_num)[1:-1])
print('Нужно чисел:', len(result))
print('Список чисел:', str(result)[1:-1])
