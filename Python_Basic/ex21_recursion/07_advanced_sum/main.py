def summ(*args):
    num = 0
    if isinstance(args[0], int):
        args_list = args
    else:
        args_list = args[0]
    for unit in args_list:
        if isinstance(unit, int):
            num += unit
        else:
            num += summ(unit)
    return num


print(summ([[1, 2, [3]], [1], 3]))

print(summ(1, 2, 3, 4, 5))