# address = '134.255.-242.189'

address = '777.255.242.189'


def fnk(cell):
    if cell.isdigit():
        if int(cell) >= 0 and int(cell) <= 255:
            responce = 'IP-адрес корректен'
        else:
            responce = str(cell) + ' выходит из диапазона от 0 до 255'
    else:
        responce = str(cell) + ' не целое число'
    return responce


address_list = address.split('.')

if len(address_list) != 4:
    print('Адрес - это четыре числа, разделенные точками')
else:
    for list_loop in address_list:
        results = fnk(list_loop)
        if results != 'IP-адрес корректен':
            print(results)
            break
    else:
        print('IP-адрес корректен')