def tower_of_hanoi(numbers, start, end):
    if numbers == 1:
        print(f'Переложить диск 1 со стержня {start} на стержень {end}')
        return
    else:
        tmp = 6 - start - end
        tower_of_hanoi(numbers - 1, start, tmp)
        print(f'Переложить диск {numbers} со стержня {start} на стержень {end}')
        tower_of_hanoi(numbers - 1, tmp, end)


numbers = int(input('Кол-во дисков: '))
tower_of_hanoi(numbers, 1, 2)

# зачёт!
