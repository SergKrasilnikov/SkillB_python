import random

stick = int(input('Кол-во палок: '))
stone = int(input('Кол-во бросков: '))

field = ['I' for i in range(stick)]

for stone_loop in range(stone):
    a = random.randint(0, stick - 1)
    b = random.randint(0, stick - 1)
    for range_loop in range(min(a, b), max(a, b) + 1):
        field[range_loop] = '.'
    print('Бросок ' + str(stone_loop + 1) + '. Сбиты палки с номера '
          + str(min(a, b) + 1) + ' по номер ' + str(max(a, b) + 1))

print('\nРезультат:', ''.join(field))

# COMMENT второй способ
# for stone_loop in range(stone):
#     a = random.randint(0, stick - 1)
#     b = random.randint(0, stick - 1)
#     if b < a:
#         a = a + b; b = a - b; a = a - b
#     for range_loop in range(a - 1, b):
#         field[range_loop] = '.'
#     print('Бросок ' + str(stone_loop + 1) + '. Сбиты палки с номера '
#           + str(a) + ' по номер ' + str(b))
#
# print('\nРезультат:', ''.join(field))