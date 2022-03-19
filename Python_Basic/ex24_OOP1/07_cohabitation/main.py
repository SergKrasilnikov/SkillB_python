import random

class House:
    meal = 50
    money = 0

class Man:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.my_home = None

    def registration(self, home):
        if isinstance(home, House):
            self.my_home = home
            print(f'{self.name} at home.')

    def eat(self):
        if self.my_home.meal > 0:
            self.health += 1
            self.my_home.meal -= 1
            return 'eating.'

    def shop(self):
        if self.my_home.money > 0:
            self.my_home.money -= 1
            self.my_home.meal += 1
            return 'go shopping.'

    def work(self):
        self.health -= 1
        self.my_home.money += 1
        return 'working.'

    def information(self):
        print(f'Name: {self.name}; Health: {self.health}; Meal: {self.my_home.meal}; Money: {self.my_home.money}.')

    def play(self):
        self.my_home.meal -= 1
        return 'play in games.'

    def one_day(self):
        dice = random.randint(1, 6)
        if self.health < 0:  # die
            return self.name
        if self.health < 20 and self.my_home.meal >= 10:
            text = self.eat()
        elif self.my_home.meal < 10:
            text = self.shop()
        elif self.my_home.money < 50:
            text = self.work()
        elif dice == 1:
            text = self.work()
        elif dice == 2:
            text = self.eat()
        else:
            text = self.play()
        print(self.name, text)
        return None

home = House()
tom = Man('Tom')
bob = Man('Bob')
tom.registration(home)
bob.registration(home)

for day in range(1, 366):  # let's start
    print(f'\nDay: {day}')
    day_tom = tom.one_day()
    day_bob = bob.one_day()
    Man.information(tom)
    Man.information(bob)
    if day_tom == 'Tom':
        print('Tom is dead.')
        break
    if day_bob == 'Bob':
        print('Bob is dead.')
        break