people = int(input('Кол-во человек: '))
shot = int(input('Число выбывшего: '))
people_list = []
index = 0

for people_loop in range(people):
    people_list.append(people_loop + 1)
print('Текущий круг:', people_list)

while len(people_list) > 1:
    print('\nТекущий круг людей:', people_list)
    print('Начало счета с номера:', people_list[index])
    for people_game in range(shot):
        if people_game + 1 == shot:
            print('Выбывает человек под номером:', people_list[index])
            people_list.pop(index)
            index -= 1
        index += 1
        if index == len(people_list):
            index = 0

print('\nОстался человек под номером:', *people_list)
