def search(x, y, r):
    if abs(x) <= r and abs(y) <= r:
        print('Монетка где-то рядом\n')
    else:
        print('Монетки в области нет\n')


while True:
    print('\nВведите воординаты монетки:')
    x = float(input('Х: '))
    y = float(input('Y: '))
    r = int(input('Введите радиус: '))
    search(x, y, r)

# зачёт!
