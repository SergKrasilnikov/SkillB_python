def shift_func(word, shift):
    char_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym != ' ' else ' ') for sym in word]
    new_world = ''
    for char_loop in char_list:
        new_world += char_loop
    return new_world


word = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

result = shift_func(word, shift)

print('Зашифрованное сообщение:', result)

# COMMENT второе решение через ASCII
# new_world = []
# index = 0
#
# for i in word:
#     index = ord(i)
#     if ord(i) >= ord('а') and ord(i) <= ord('я'):
#         index = ord(i) + shift
#         if index < ord('а'):
#             index = ord('я') - (ord('а') - index) + 1
#         elif index > ord('я'):
#             index = ord('а') + (index - ord('я')) - 1
#
#     new_world.append(chr(index))
#
# print('Зашифрованное сообщение:', ''.join(new_world))