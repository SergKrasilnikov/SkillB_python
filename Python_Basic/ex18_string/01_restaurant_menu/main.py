in_menu = input('Доступное меню: ')
list_menu = in_menu.split(';')

out_menu = ', '.join(list_menu)

print('На данный момент в меню есть:', out_menu)