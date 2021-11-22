shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]
summ = count = 0

avail = input('Название детали: ')

for search_loop in shop:
    if search_loop[0] == avail:
        summ += search_loop[1]
        count += 1

print('Кол-во деталей -', count)
print('Общая стоимость -', summ)
