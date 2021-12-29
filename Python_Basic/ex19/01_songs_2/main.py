violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

num = int(input('Кол-во песен: '))
total_time = 0

for num_loop in range(1, num + 1):
    name_dict = input('Название ' + str(num_loop) + ' песни: ')
    if violator_songs.get(name_dict, None):
        total_time += violator_songs.get(name_dict)
    else:
        print('Такой песни нет.')

print('\nОбщее время звучания песен: {} минут.'.format(total_time))