num = int(input('Введите длину списка: '))

result = [(1 if place % 2 == 0 else place % 5) for place in range(num)]

print('Результат: ', result)