from operator import itemgetter

tries = int(input('Кол-во записей в протоколе: '))

tries_dict = {}
print('Записи (результат и имя):')
for i in range(tries):
    number, name = input(f'{i + 1} запись: ').split()
    number = int(number)

    if name in tries_dict:
        if number > tries_dict[name][0]:
            tries_dict[name][0] = number
    else:
        tries_dict[name] = [number]

scores = list(tries_dict.items())
print(scores)
print('\nИтоги соревнований:')

for i in range(2):
    sort = sorted(scores, key=itemgetter(1), reverse=True)[i]
    print(f' {i + 1} место {sort[0]} ({sort[1][0]})')