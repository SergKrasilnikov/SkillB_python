def shift_func(word, shift):
    char_list = [(alphabet[(alphabet.index(sym) + shift) % 52] if sym != ' ' or sym == r'\\' else ' ') for sym in word]
    new_world = ''
    for char_loop in char_list:
        new_world += char_loop
    return new_world

shift = 0
alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

initial_file = open('text.txt', 'w+')
initial_file.write('Hello\nHello\nHello\nHello')
initial_file.seek(0)
shifted_file = open('cipher_text.txt', 'a')

for i_line in initial_file:
    shift += 2

    if '\n' in i_line:
        result = shift_func(i_line[:len(i_line) - 1], shift)
    else:
        result = shift_func(i_line, shift)

    shifted_file.write(result + '\n')


initial_file.close()
shifted_file.close()