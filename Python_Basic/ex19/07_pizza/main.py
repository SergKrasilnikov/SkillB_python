def get_word(d, word):
    value = d.get(word[0])
    if value.get(word[1]) is None:
        value[word[1]] = int(word[2])
    else:
        value[word[1]] = value.get(word[1]) + int(word[2])

def get(d, v):
    if v[0] in d.keys():
        get_word(d, v)
    else:
        d[v[0]] = {v[1]: int(v[2])}
    return d

customer = {}
num = int(input('Введите кол-во заказов: '))

for index in range(1, num + 1):
    value = input('{} заказ: '.format(index)).lower().split()
    get(customer, value)

for i_info in customer:
    print('{}:'.format(i_info.capitalize()))
    for info in customer[i_info]:
        print('\t\t{}: {}'.format(info.capitalize(), customer[i_info][info]))