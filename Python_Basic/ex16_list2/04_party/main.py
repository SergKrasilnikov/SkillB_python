guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
status = ['']

while status[0] != 'Пора спать':
    print('\nСейчас на вечеринке ' + str(len(guests)) + ' человек: ' + str(guests))
    status.pop(0)
    status.append(input('Гость пришел или ушел?'))

    if status[0] == 'пришел':
        name = input('Имя гостя: ')
        if len(guests) <= 5:
            print('Привет, ' + name + '!')
            guests.append(name)
        else:
            print('Прости, ' + name + ', но мест нет.')

    elif status[0] == 'ушел':
        name = input('Имя гостя: ')
        if name not in guests:
            print('Таких нет.')
        else:
            print('Пока, ' + name + '!')
            guests.remove(name)

print('\nВечеринка закончилась, все легли спать.')
