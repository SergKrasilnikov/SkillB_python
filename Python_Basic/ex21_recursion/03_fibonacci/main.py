def fib(num):
    if num == 0 or num == 1:
        return num
    else:
        return fib(num - 2) + fib(num - 1)


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
pos = fib(num_pos)
print(pos)

# зачёт!
