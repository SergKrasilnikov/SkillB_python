num = int(input('Кол-во клеток: '))
cell_index = []

for num_loop in range(1, num + 1):
    print('Эффективность', num_loop, end = ' ')
    index = int(input('клетки: '))

    if num_loop > index:
        cell_index.append(index)

print('\nНеподходящие значение:', cell_index)


