a_list = [1, 5, 3]  # основной
b_list = [1, 5, 1, 5]  # побочный 1
c_list = [1, 3, 1, 5, 3, 3]  # побочный 2

a_list.extend(b_list)
count = a_list.count(5)
print('Кол-во цифр 5 при повторном объединении:', count)

for _ in range(count):
    a_list.remove(5)

a_list.extend(c_list)
count = a_list.count(3)
print('Кол-во цифр 3 при повторном объединении:', count)
print('Итоговый список:', a_list)

# COMMENT Изначальный код.
# a = [1, 5, 3] # основной
# b = [1, 5, 1, 5] # побочный 1
# c = [1, 3, 1, 5, 3, 3] # побочный 2
#
# for i in b:
#     a.append(i)
# print(a)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1 # подсчет 5-ок
# print('Кол-во цифр 5 при повторном объединении:', t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i) # копирование в новый список d из списка a всех не 5-ок
# print(d)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1 # подсчет 3-ок
# print('Кол-во цифр 3 при повторном объединении:', t)
# print('Итоговый список:', d)
