def contains_only_integers(tup):
    for item in tup:
        if not isinstance(item, int):
            return tup
    return tuple(sorted(tup))


tuple_num = (6, 3, -1, 8, 4, 10, -5)

print(contains_only_integers(tuple_num))