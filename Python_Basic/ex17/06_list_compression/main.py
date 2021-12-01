def num_remover(num_list):
    count = 0
    for _ in range(num_list.count(0)):
        num_list.remove(0)
        count += 1
    return num_list, count

num_list = [1, 4, 2, 5, 0, 5, 4, 0, 8]

num_list, count = num_remover(num_list)

for _ in range(count):
    num_list.append(0)

print(num_list)

num_list, count = num_remover(num_list)

print(num_list)

# COMMENT второй способ

# def num_remover(num_list):
#     for _ in range(num_list.count(0)):
#         num_list.remove(0)
#     return num_list
#
# def num_mover(num_list):
#     for _ in range(num_list.count(0)):
#         num_list.remove(0)
#         num_list.append(0)
#     return num_list
#
# num_list = [1, 4, 2, 5, 0, 5, 4, 0, 8]
#
# num_list = num_mover(num_list)
#
# print(num_list)
#
# num_list = num_remover(num_list)
#
# print(num_list)