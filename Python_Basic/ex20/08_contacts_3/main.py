def add_name():
    name = input('Введите имя и фамилию нового контакта (через пробел): ')

    name = name.split()[0], name.split()[1]
    number = input('Введите номер телефона: ')
    if name not in name_dict:
        name_dict[name] = number
    else:
        print('Такой человек уже есть в контактах.')
    print('Текущие контакты:', name_dict)


def search_name():
    name = input('Введите фамилию: ')

    for key, value in name_dict.items():
        if name.lower() in key[0].lower() or name.lower() + 'а' in key[0].lower():
            print(key[0], key[1], value)
        else:
            print('Такого человека нет в контактах.')


name_dict = {}
while True:
    question = int(input('\nВведите номер действия:\n   1. Добавить контакт\n   2. Найти человека\n'))

    if question == 1:
        add_name()
    elif question == 2:
        search_name()