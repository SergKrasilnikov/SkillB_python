def zip_for_life(in_string, number_tuple):
    min_list = min(len(in_string), len(number_tuple))

    return [(in_string[i], number_tuple[i]) for i in range(min_list)]

in_string = 'abcd'
number_tuple = (10, 20, 30, 40)

# in_string = [{'x': 4}, 'b', 'z', 'd']
# number_tuple = (10, {20,}, [30], 'z')

print(zip_for_life(in_string, number_tuple))