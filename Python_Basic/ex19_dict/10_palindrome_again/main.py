def poly(word):
    char_dict = {}
    for i_sym in word:
        char_dict[i_sym] = char_dict.get(i_sym, 0) + 1
    count = 0
    for i_val in char_dict.values():
        if i_val % 2 != 0:
            count += 1
    return count <= 1


text = input('Введите строку: ')

if poly(text):
    print('Можно сделать палиндромом.')
else:
    print('Нельзя сделать палиндромом.')

# зачёт!
