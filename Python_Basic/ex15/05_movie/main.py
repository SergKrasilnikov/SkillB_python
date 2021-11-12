films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
in_love = []

while True:
    question = input('\nВведите название фильма: ')

    for film_list in films:
        if film_list == question:
            in_love.append(film_list)
            print('Фильм найден!')
            break
    else:
        print('Такого фильма нет.')

    print('Список любимых фильмов:', in_love)
