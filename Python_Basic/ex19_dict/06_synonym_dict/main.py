def get_word(d, word):
    for key, value in d.items():
        if value == word:
            return key
        elif key == word:
            return value

dictionary = dict()
num = int(input('Кол-во пар слов: '))

for index in range(1, num + 1):
    value = input('{} пара: '.format(index)).lower().split(' - ')
    dictionary[value[1]] = value[0]
    dictionary[value[0]] = value[1]

while True:
    search = input('Введите слово: ')
    search.lower()
    result = get_word(dictionary, search.lower())
    if result is None:
        print('Такого слова в словаре нет.')
    else:
        print('Синоним:', result)
        break

#COMMENT второй вариант.

# for index in range(1, num + 1):
#     value = input('{} пара: '.format(index)).lower().split()
#     for word in value[1:]:
#         if word != '-':
#             dictionary[word] = value[0]
#
# while True:
#     search = input('Введите слово: ')
#     search.lower()
#     result = get_word(dictionary, search.lower())
#     if result is None:
#         print('Такого слова в словаре нет.')
#     else:
#         print('Синоним:', result)
#         break