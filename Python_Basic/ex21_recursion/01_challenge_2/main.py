def recursion(max_num):
    if max_num != 1:
        recursion(max_num - 1)
    print(max_num)


max_num = int(input('Конечное значение: '))
recursion(max_num)

# COMMENT чуть кривее вариант

# def recursion(n):
#     if n == max:
#         print(n)
#     else:
#         print(n)
#         recursion(n + 1)
#
# max = int(input('Конечное значение: '))
# recursion(1)

# COMMENT по убыванию.

# def recursion(n):
#     if n == 1:
#         print(1)
#         print('this is the end')
#     else:
#         print(n)
#         recursion(n - 1)
#
# num = int(input('Конечное значение: '))
# recursion(num)

# зачёт!
