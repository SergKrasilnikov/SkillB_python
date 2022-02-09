def place_found(old_list, new):
    place = 0
    for weight_list in old_list:
        place += 1
        if new > weight_list:
            break
    return place


quantity = int(input('Кол-во контейнеров: '))
place_old = []

for _ in range(quantity):
    weight = int(input('Введите вес контейнера: '))
    while weight <= 0 or weight > 200:
        weight = int(input('Введите вес контейнера: '))
    if weight > 0 and weight <= 200:
        place_old.append(weight)

weight_new = int(input('\nВведите вес нового контейнера: '))
while weight_new <= 0 or weight_new > 200:
    weight_new = int(input('\nВведите вес нового контейнера: '))

place = place_found(place_old, weight_new)

print('\nНомер, куда встанет новый контейнер:', place)
