in_string = 'abcd'
number_tuple = (10, 20, 30, 40)

in_list = list(in_string)
number_list = list(number_tuple)

min_list = min(len(in_list), len(number_list))

generator = ((in_list[i], number_tuple[i]) for i in range(min_list))

print(generator)
for unit in generator:
    print(unit)