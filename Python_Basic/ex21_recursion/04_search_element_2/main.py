site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def key_search(struct, key, depth):
    if depth == 1 or depth <= 0:
        if key in struct:
            return struct[key]
    if depth <= 0 or depth > 1:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = key_search(sub_struct, key, depth - 1)
                if result:
                    break
        else:
            result = None
        return result


user_key = input('Название ключа: ')
question = input('Ввести максимальную глубину поиска (yes/no)?: ')
max_depth = 0
if question == 'yes':
    max_depth = int(input('Максимальная глубина: '))
value = key_search(site, user_key, max_depth)

if value:
    print(value)
else:
    print('Ключ отсутствует.')