import random

def first_func(x, y):
        x += random.randint(0, 10)
        y += random.randint(0, 5)
        return x / y

def second_func(x, y):
        x -= random.randint(0, 10)
        y -= random.randint(0, 5)
        return y / x

with open('coordinates.txt', 'w') as file:
    file.write('5 10\n2 4')

try:
    with open('coordinates.txt', 'r') as file:
        for line in file:
            nums_list = line.split()
            try:
                res1 = first_func(int(nums_list[0]), int(nums_list[1]))
            except ZeroDivisionError:
                res1 = 0
                print('ZeroDivisionError in first function.')
            try:
                res2 = second_func(int(nums_list[0]), int(nums_list[1]))
            except ZeroDivisionError:
                res2 = 0
                print('ZeroDivisionError in second function.')

            number = random.randint(0, 100)
            with open('result.txt', 'a') as file_2:
                my_list = sorted([res1, res2, number])
                file_2.write(str(my_list) + '\n')
except Exception:
        print("Something went wrong.")



# try:
#     with open('coordinates.txt', 'r') as file:
#         for line in file:
#             nums_list = line.split()
#             print(nums_list)
#             res1 = f(int(nums_list[0]), int(nums_list[1]))
#             print(res1)
#             try:
#                 res2 = f2(int(nums_list[0]), int(nums_list[1]))
#                 print(res2)
#                 try:
#                     number = random.randint(0, 100)
#                     print(number)
#                     with open('result.txt', 'a') as file_2:
#                         my_list = sorted([res1, res2, number])
#                         file_2.write(str(my_list) + '\n')
#                 except Exception:
#                     print("Что-то пошло не так")
#             except Exception:
#                 print("Что-то пошло не так со второй функцией")
#             # finally:
# except Exception:
#     print("Что-то пошло не так с первой функцией")