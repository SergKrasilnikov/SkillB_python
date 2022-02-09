import random

def random_func():
    return [(random.randint(0, 10), random.randint(0, 10)) for i in range(0, 10, 2)]

a = random_func()
pairs = list(a)
print(pairs)

# COMMENT "Дополнительно": один из способов.
# def random_func():
#     return [random.randint(0, 10) for _ in range(5)]
#
# a = random_func()
# b = random_func()
# pairs = list(zip(a, b))
# print(pairs)

# COMMENT "Дополнительно": один из способов.
# def random_func():
#     return [(random.randint(0, 10), random.randint(0, 10)) for _ in range(0, 5)]
#
# a = random_func()
# pairs = list(a)
# print(pairs)