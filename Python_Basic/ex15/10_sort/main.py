# COMMENT первый вариант
def bubble(array):
    for a in range(quantity - 1):
        for b in range(quantity - a - 1):
            if array[b] > array[b + 1]:
                buff = array[b]
                array[b] = array[b + 1]
                array[b + 1] = buff
    return array


while True:
    quantity = int(input('\nКол-во значений: '))
    enter_list = []
    for _ in range(quantity):
        enter_list.append(int(input('Введите число для сортировки: ')))

    print('Изначальный список:', enter_list)
    enter_list = bubble(enter_list)
    print('Отсортированный список:', enter_list)

# COMMENT второй вариант
# print(sorted(enter_list))

# COMMENT третий вариант
# enter_list.sort()
