def num_list(a, b):
    num = []
    for _ in range(a):
        num_loop = int(input(str(b) + ' список. Введите число: '))
        num.append(num_loop)
    return num


first_list = num_list(3, 1)
second_list = num_list(7, 2)
print('\nПервый список:', first_list)
print('Второй список:', second_list)

first_list.extend(second_list)
print(first_list)

for num_loop in first_list:
    count = first_list.count(num_loop)

    for count_loop in range(count - 1):
        first_list.remove(num_loop)

print('\nУникальные элементы:', first_list)

# COMMENT второй вариант решения

# print(list(set(first_list)))

# COMMENT третий вариант

# def num_list(a, b):
#     num = []
#     for _ in range(a):
#         num_loop = int(input(str(b) + ' список. Введите число: '))
#         num.append(num_loop)
#     return num
#
# first_list = num_list(3, 1)
# second_list = num_list(7, 2)
# print('\nПервый список:', first_list)
# print('Второй список:', second_list)
#
# first_list.extend(second_list)
#
# size = len(first_list)
# index = count = 0
#
# for num_loop in range(len(first_list)):
#     count = first_list.count(first_list[index])
#
#     for count_loop in range(count - 1):
#         first_list.remove(first_list[num_loop])
#         count = 0
#         size -= 1
#         index -= 1
#     index += 1
#
# print('\nУникальные элементы:', first_list)
