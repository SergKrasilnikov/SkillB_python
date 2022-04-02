list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

def func(ls1: list, ls2: list) -> tuple:
    for x in ls1:
        for y in ls2:
            result = x * y
            yield x, y, result

func_res = func(list_1, list_2)

for i_num in func_res:
    print(i_num)
    if i_num[0] * i_num[1] == to_find:
        print(f'The result is number {i_num[0]} and number {i_num[1]}.')
        break

# Нужно найти какие два числа из списков в результате попарного перемножения дадут число 56
# list_1 = [2, 5, 7, 10]
# list_2 = [3, 8, 4, 9]
# to_find = 56
#
# can_continue = True
# for x in list_1:
#     for y in list_2:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break