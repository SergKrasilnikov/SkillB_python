# COMMENT решение, которое работает только в узком диапазоне значений. Со всеми возможными комбинациями оно не будет\
#  работать. ('.Это. задание ,. очень! простое. возм:ожно'). Но если это требуется - welcome.
word = 'Хотя ,. возм:ожно и нет.'

word_1 = ''
word_2 = ''
word_3 = ''

list_text = word.split(' ')

for list_loop in range(len(list_text)):
    if list_text[list_loop].isalpha():
        list_text[list_loop] = list_text[list_loop][::-1]
    else:
        inner_word = list_text[list_loop]
        for i in range(len(list_text[list_loop])):
            if not list_text[list_loop][i].isalpha():
                word_1 = list_text[list_loop][:i]
                word_2 = list_text[list_loop][i]
                word_3 = list_text[list_loop][i + 1:]
                list_text[list_loop] = word_1[::-1] + word_2 + word_3[::-1]

print('Новое сообщение:', ' '.join(list_text))

# COMMENT гениальное применение ASCII. Которое работает в любом случае.
# def fnk(word, result, symbol):
#     word.reverse()
#     word.append(symbol)
#     result.extend(word)
#     word.clear()
#     return word, result
#
# word = '.Это. задание ,. очень! простое. .возм:ожно/'
#
# new_world = []
# res_world = []
#
# for i in word:
#     if ord(i) >= ord('а') and ord(i) <= ord('я') or ord(i) >= ord('А') and ord(i) <= ord('Я'):
#         new_world.append(i)
#     elif ord(i) == ord(' ') or ord(i) >= ord('!') and ord(i) <= ord('@'):
#         new_world, res_world = fnk(new_world, res_world, i)
#
# if len(new_world) != 0:
#     if ord(new_world[0]) >= ord('а') and ord(new_world[0]) <= ord('я') \
#         or ord(new_world[0]) >= ord('А') and ord(new_world[0]) <= ord('Я'):
#         new_world, res_world = fnk(new_world, res_world, new_world[0])
#
# print('Новое сообщение:', ''.join(res_world))