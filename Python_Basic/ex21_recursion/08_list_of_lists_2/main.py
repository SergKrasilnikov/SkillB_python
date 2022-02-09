def summ(*args):
    if not args:
        return []
    num = []
    if isinstance(args[0], int):
        args_list = args
    else:
        args_list = args[0]
    for unit in args_list:
        if isinstance(unit, int):
            num.append(unit)
        else:
            num += summ(unit)
    return num


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(summ(nice_list))

# COMMENT не менее гениальный вариант

# def summ(*args):
#     num = []
#     if isinstance(args[0], int):
#         args_list = args
#     else:
#         args_list = args[0]
#     for unit in args_list:
#         if isinstance(unit, int):
#             num.append(unit)
#         else:
#             for i_unit in summ(unit):
#                 num.append(i_unit)
#     return num

# COMMENT второй вариант.

# def summ(*args):
#     num = 0
#     if args == []:
#         return []
#
#     def flatten(a_list):
#         num = []
#         for unit in a_list:
#             if isinstance(unit, int):
#                 num.append(unit)
#             else:
#                 num.extend(flatten(unit))
#         return num
#
#     return flatten(args)