in_string = 'abchytrewqhcba'

part_1 = in_string[:in_string.find('h') + 1]
part_2 = in_string[in_string.find('h') + 1:in_string.rfind('h')]
part_3 = in_string[in_string.rfind('h'):]

result = part_1 + part_2[::-1] + part_3

print(result)