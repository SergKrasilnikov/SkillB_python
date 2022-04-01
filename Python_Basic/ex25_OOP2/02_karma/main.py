import random

class KillError(Exception):
    def __str__(self):
        return 'KillError'

class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError'

class CarCrashError(Exception):
    def __str__(self):
        return 'CarCrashError'

class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError'

class DepressionError(Exception):
    def __str__(self):
        return 'DepressionError'

def one_day(day):
    points = random.randint(1, 7)
    if random.randint(1, 10) == 1:
        print('hah')
        with open('karma.log', 'a') as karma_out:
            dice_unit = random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
            karma_out.write(f'Day: {day}. {dice_unit}\n')

    return points

day = carma = 0
while True:
    day += 1
    print(f'Day {day}.')
    day_carma = one_day(day)
    print(f'In this day you have {day_carma} points.')
    carma += day_carma
    if carma >= 500:
        print('You are Holly!')
        break