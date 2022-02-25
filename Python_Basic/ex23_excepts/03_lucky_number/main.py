import random

number_file = open('numbers.txt', 'w')
number_file.close()

summ = 0
while True:
    num = int(input('Type number: '))
    dice = random.randint(1, 13)
    print(dice)
    if dice == 13:
        print('What a shame!')
        raise random.choice([NameError, SyntaxError, ValueError, IndexError])

    with open('numbers.txt', 'a+') as number_file:
        number_file.write(str(num) + '\n')
    summ += num
    print(summ)
    if summ >= 777:
        print('You are perfect!')
        break