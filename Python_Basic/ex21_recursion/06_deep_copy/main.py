import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам iphone недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def key_search(struct, word, count=4):
    a = list(struct.keys())
    key_tmp = a[0]
    for key, value in struct.items():
        if key_tmp != key:
            print(',')
        print(count * ' ' + "'" + str(key) + "'" + ': ', end='')
        if isinstance(value, dict):
            print('{')
            key_search(value, word, count + 4)
            print(count * ' ' + '}')
        else:
            print("'" + value.replace('iphone', word) + "'")
    return


num = int(input('Кол-во сайтов: '))
for i in range(num):
    user_name = input('Введите название продукта для нового сайта: ')
    print('site = {')
    value = key_search(copy.deepcopy(site), user_name)
    print('}')

# COMMENT вариант с не изменяемыми ключами.

# def key_search(struct, value):
#     key1 = 'title'
#     key2 = 'h2'
#     if key1 in struct:
#         struct[key1] = (f'Куплю/продам {value} недорого')
#     if key2 in struct:
#         struct[key2] = (f'У нас самая низкая цена на {value}')
#         return site
#     for sub_struct in struct.values():
#         if isinstance(sub_struct, dict):
#             result = key_search(sub_struct, value)
#             if result:
#                 break
#     else:
#         result = None
#     return result

# num = int(input('Кол-во сайтов: '))
# for i in range(num):
#     user_name = input('Введите название продукта для нового сайта: ')
#     value = key_search(site, user_name)
#     if value:
#         print(value)
#     else:
#         print('Ключ отсутствует.')