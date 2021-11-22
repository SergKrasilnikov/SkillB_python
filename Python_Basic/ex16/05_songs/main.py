violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

num = int(input('Сколько песен выбрать? '))
count = 0
song = ''

for num_loop in range(num):
    song = (input('Название ' + str(num_loop + 1) + ' песни: '))
    for song_loop in violator_songs:
        if song_loop[0] == song:
            count += song_loop[1]
            break

print('Общее время звучания песен:', count)
