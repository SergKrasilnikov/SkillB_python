def recur_factorial(n, factorials):
    if n in factorials:
        return factorials[n]
    elif n == 1:
        return n
    else:
        return n * recur_factorial(n - 1, factorials)


def calculating_math_func(data, factorials={}):
    if data in factorials:
        result = factorials[data]
    else:
        result = recur_factorial(data, factorials)
        factorials[data] = result
    result /= data ** 3
    result = result ** 10
    return result


while True:
    num = int(input('Входное число: '))
    a = calculating_math_func(num)
    print(a)

# зачёт!
