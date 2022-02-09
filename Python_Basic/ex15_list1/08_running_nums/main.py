# COMMENT первое решение задачи.
def perpetuity(list_old, move):
    for _ in range(move):
        last = list_old[len(list_old) - 1]
        for list_loop in range(len(list_old) - 1, 0, -1):
            list_old[list_loop] = list_old[list_loop - 1]
        list_old[0] = last

    return list_old


# COMMENT второе решение задачи
# def perpetuity(list_old, move):
#     cut = []
#     list_new = []
#     index = len(list_old) - move
#
#     for list_loop in list_old:
#         if index > 0:
#             cut.append(list_loop)
#             index -= 1
#
#     for _ in range(move):
#         list_new.append(list_old[-move])
#         move -= 1
#
#     for num_loop in cut:
#         list_new.append(num_loop)
#
#     return list_new

# while True:
#     move = int(input('Сдвиг: '))
#     list_old = [1, 2, 3, 4, 5]
#
#     list_new = perpetuity(list_old, move)
#
#     print('Изначальный список:', list_old)
#     print('Сдвинутый список:', list_new)

while True:
    move = int(input('Сдвиг: '))
    list_old = [1, 2, 3, 4, 5]
    print('Изначальный список:', list_old)

    list_new = perpetuity(list_old, move)

    print('Сдвинутый список:', list_old)
