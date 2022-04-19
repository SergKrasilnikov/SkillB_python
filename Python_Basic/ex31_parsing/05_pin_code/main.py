import itertools

variables = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0
for item in itertools.combinations_with_replacement(variables, 4):
    count += 1
    print(item)

print(f'Possible combinations: {count}')