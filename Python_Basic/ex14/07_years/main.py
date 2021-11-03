start = int(input('Введите первый год: '))
end = int(input('Введите второй год: '))

print('\nГода от', start, 'до', end, 'с тремя одинаковыми цифрами:')

for year_loop in range(start, end + 1):
    count = 0
    a = year_loop // 1000
    b = (year_loop // 100) % 10
    c = (year_loop // 10) % 10
    d = year_loop % 10

    if a == b and a == c:
        print(year_loop)
    elif a == b and a == d:
        print(year_loop)
    elif a == c and a == d:
        print(year_loop)
    elif b == c and b == d:
        print(year_loop)