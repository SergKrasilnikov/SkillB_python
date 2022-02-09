goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for key, value in goods.items():
    quantity = 0
    price = 0
    for store_loop in store.get(value):
        quantity += store_loop.get('quantity')
        price += store_loop.get('price') * store_loop.get('quantity')
    print('{} - {} шт, стоимость {} руб.'.format(key, quantity, price))


#COMMENT второй вариант.

# for goods_loop in goods:
#     quantity = 0
#     price = 0
    # for store_loop in range(len(store[goods.get(goods_loop)])):
    #     quantity += store[goods.get(goods_loop)][store_loop]['quantity']
    #     price += store[goods.get(goods_loop)][store_loop]['quantity'] *\
    #              store[goods.get(goods_loop)][store_loop]['price']
    #
    # print('{} - {} шт, стоимость {} руб.'.format(goods_loop, quantity, price))