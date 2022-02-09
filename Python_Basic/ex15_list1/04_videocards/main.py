gcard_num = int(input('Кол-во видеокарт: '))

old_gcard = []
new_gcard = []
max_num = 0

for num_loop in range(1, gcard_num + 1):
    print(num_loop, end=' ')
    card_index = int(input('Видеокарта: '))
    old_gcard.append(card_index)
    if card_index > max_num:
        max_num = card_index

for max_loop in old_gcard:
    if max_loop != max_num:
        new_gcard.append(max_loop)

print('\nСтарый список видеокарт:', old_gcard)
print('\nНовый список видеокарт:', new_gcard)
