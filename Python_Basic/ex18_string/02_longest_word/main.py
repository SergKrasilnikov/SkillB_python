text = input('Текст: ')

list_text = text.split(' ')
result = max(list_text, key=len)

print('Самое длинное слово:', result, 'Кол-во символов:', len(result))