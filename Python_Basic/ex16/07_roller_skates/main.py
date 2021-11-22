rol_size = []
foot_size = []
count = 0

rol_num = int(input('Кол-во коньков: '))

for rol_loop in range(rol_num):
    rol_size.append(int(input('Размер ' + str(rol_loop + 1) + ' пары: ')))

rol_size.sort()

foot_num = int(input(('\nКол-во людей: ')))

for foot_loop in range(foot_num):
    foot_size.append(int(input('Размер ноги ' + str(foot_loop + 1) + ' человека: ')))

    for rol_in_loop in rol_size:
        if rol_in_loop >= foot_size[foot_loop]:
            rol_size.remove(rol_in_loop)
            count += 1
            break

print('\nНаибольшее кол-во людей с роликами:', count)

# COMMENT второй вариант решения.
# for rol_loop in range(rol_num):
#     rol_size.append(int(input('Размер ' + str(rol_loop + 1) + ' пары: ')))
#
# foot_num = int(input(('\nКол-во людей: ')))
#
# for foot_loop in range(foot_num):
#     foot_size.append(int(input('Размер ноги ' + str(foot_loop + 1) + ' человека: ')))
#
#     close_size = 100
#     for rol_in_loop in rol_size:
#         if rol_in_loop >= foot_size[foot_loop]:
#             rol_size.remove(rol_in_loop)
#             count += 1
#             break
#         elif rol_in_loop > foot_size[foot_loop]:
#             if rol_in_loop < close_size:
#                 close_size = rol_in_loop
#     if close_size < 100:
#         rol_size.remove(close_size)
#         count += 1
#
# print('\nНаибольшее кол-во людей с роликами:', count)
