def search(tpl):
    unit = int(input('Элемент для поиска: '))
    count = tpl.count(unit)

    if count == 0:
        return ()
    elif count == 1:
        return tuple(tpl[tpl.index(unit):])
    else:
        first = tpl.index(unit)
        return tuple(tpl[first:tpl.index(unit, first + 1, len(tpl)) + 1])

# tpl = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
#
# print(search(tpl))