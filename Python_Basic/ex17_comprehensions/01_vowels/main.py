text = input('Введите текст: ')
result_list = []

vowels = ['а', 'у', 'о', 'и', 'э', 'ы', 'я', 'ю', 'е', 'ё']
result_list = [text_loop for text_loop in text if text_loop in vowels]

print('Список гласных букв:', result_list)
print('Длина списка:', len(result_list))

#COMMENT второй вариант

# for text_loop in text:
#     if text_loop in vowels:
#         result_list.append(text_loop)

# print('Список гласных букв:', result_list)
# print('Длина списка:', len(result_list))