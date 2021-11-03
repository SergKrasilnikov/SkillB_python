def calc(num):
    index = results = num
    while index != 1:
        if (num % index) == 0:
            results = index
            index -= 1
        else:
            index -= 1
    return results


while True:
    num = int(input('\nВведите первое число: '))
    results = calc(num)

    print('Наименьший делитель, отличный от единицы:', results)

# зачёт!
