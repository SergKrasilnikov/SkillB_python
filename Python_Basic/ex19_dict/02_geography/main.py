city_dict = dict()
num = int(input('Кол-во стран: '))

for index in range(1, num + 1):
    value = input('{} страна: '.format(index)).split()
    for town in value[1:]:
        city_dict[town] = value[0]

for index in range(1, 4):
    city = input('\n{} город: '.format(index))
    country = city_dict.get(city)
    if country:
        print('Город {} расположен в стране {}.'.format(city, country))
    else:
        print('По городу {} данных нет.'.format(city))