import random

class Warrior:
    def __init__(self, name, health, hit):
        self.name = name
        self.health = health
        self.hit = hit

    def strike(self, target):
        if isinstance(target, Warrior) is False:
            print('Wrong object.')
            return 'wrong'
        else:
            if self.name == 'Warrior Tom':
                Warr_2.health -= self.hit
                print(f'{self.name} attacked {Warr_2.name}.')
                print(f'{Warr_2.name} have {Warr_2.health} health.\n')
                if Warr_2.health == 0:
                    print(f'{Warr_2.name} has died.')
                    return 'end'
            else:
                Warr_1.health -= self.hit
                print(f'{self.name} attacked {Warr_1.name}.')
                print(f'{Warr_1.name} have {Warr_1.health} health.\n')
                if Warr_1.health == 0:
                    print(f'{Warr_1.name} has died.')
                    return 'end'

Warr_1 = Warrior('Warrior Tom', 100, 20)
Warr_2 = Warrior('Warrior Bob', 100, 20)

while True:
    dice = random.randint(1, 2)
    if dice == 1:
        winner = Warr_1.strike(Warr_2)
        if winner == 'end' or winner == 'wrong':
            break
    else:
        winner = Warr_2.strike(Warr_1)
        if winner == 'end' or winner == 'wrong':
            break