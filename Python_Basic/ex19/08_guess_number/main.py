num = int(input('Введите максимальное число: '))
all_nums = set(range(1, num + 1))
possible_nums = all_nums

while True:
    guess = input('Нужное число есть среди этих чисел: ')
    if guess == 'помощь':
        break
    guess = {int(sep) for sep in guess.split()}
    answer = input('Ответ Артёма: ')
    if answer == 'да':
        possible_nums &= guess
    else:
        possible_nums &= all_nums - guess

print('Артём мог загадать следующие числа:', ' '.join([str(guess_num) for guess_num in sorted(possible_nums)]))

# зачёт!
