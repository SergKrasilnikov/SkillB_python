# COMMENT первый вариант
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

# COMMENT второй вариант
start = int(input('Введите первый год: '))
end = int(input('Введите второй год: '))

print('\nГода от', start, 'до', end, 'с тремя одинаковыми цифрами:')

while start != end:
    count = 0
    for num_loop in str(start):
        if count == 0:
            a = num_loop
            count += 1
        elif count == 1:
            b = num_loop
            count += 1
        elif count == 2:
            c = num_loop
            count += 1
        else:
            d = num_loop
    if a == b and a == c or a == b and a == d or a == c and a == d or b == c and b == d:
        print(start)
    start += 1