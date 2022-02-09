def perpetuity(first_list, second_list):
    move = 0
    result = ''

    for n in range(len(second_list)):
        if first_list == second_list:
            result = move
            break
        else:
            second_list = second_list[1:] + second_list[0]
            move += 1
            result = -1
    return result


while True:
    first_list = input('Первая строка: ')
    second_list = input('Вторая строка: ')

    result = perpetuity(first_list, second_list)

    if result == -1:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
    else:
        print('Первая строка получается из второй со сдвигом', result)