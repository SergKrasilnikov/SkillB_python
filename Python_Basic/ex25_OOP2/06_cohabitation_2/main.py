import random

class House:
    meal = 50
    money = 100
    meal_cat = 30
    dust = 0

class Person:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.mental_health = 100

    def registration(self, home):
        if isinstance(home, House):
            self.my_home = home
            print(f'{self.name} at home.')

    def eat(self):
        if self.my_home.meal > 0:
            n = self.my_home.meal / 2
            if n > 30:
                n = 30
                self.health += n
                self.my_home.meal -= n
            else:
                self.health += n
                self.my_home.meal -= n
            return 'is eating.'

    def play_cat(self):
        self.health -= 10
        self.mental_health += 5
        return 'play with cat.'

class Man(Person):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.my_home = None

    def information(self):
        print(f'Name: {self.name}; Health: {self.health}; Mental health: {self.mental_health};'
              f'Meal: {self.my_home.meal}; Money: {self.my_home.money}.')

    def play(self):
        if self.mental_health <= 80:
            self.health -= 10
            self.mental_health += 20
            return 'play in games.'

    def work(self):
        self.health -= 10
        self.my_home.money += 150
        return 'is working.'

    def one_day(self):
        self.mental_health -= 10
        if self.health < 0 or self.mental_health < 0 or self.my_home.dust > 90:  # die
            return False
        if self.health < 30 and self.my_home.meal > 0:
            text = self.eat()
        elif self.my_home.money < 50:
            text = self.work()
        else:
            text = self.play()
        print(self.name, text)
        return None

class Whife(Person):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.my_home = None

    def information(self):
        print(f'Name: {self.name}; Health: {self.health}; Mental health: {self.mental_health};'
              f'Meal: {self.my_home.meal}; Money: {self.my_home.money}.')

    def shop(self):
        if self.my_home.money >= 20:
            self.health -= 10
            self.my_home.money -= 20
            self.my_home.meal += 10
            self.my_home.meal_cat += 10
            return 'go shopping.'
        elif self.my_home.money <= 10 and self.my_home.money > 0:
            self.health -= 10
            n = self.my_home.money  # add unknown parameter
            self.my_home.money -= n
            self.my_home.meal -= n
            return 'go shopping.'

    def whife_goods(self):
        if self.my_home.money >= 400:
            self.health -= 10
            self.my_home.money -= 350
            self.mental_health += 60
            return 'wife have a goods.'

    def clean(self):
        if self.my_home.dust <= 100:
            self.health -= 10
            self.my_home.dust -= self.my_home.dust
            return 'is cleaning.'

    def one_day(self):
        self.mental_health -= 10
        if self.health < 0 or self.mental_health < 0 or self.my_home.dust > 90:  # die
            return False
        if self.health < 10 and self.my_home.meal > 0:
            text = self.eat()
        elif self.mental_health <= 80:
            text = self.play_cat()
        elif self.my_home.meal <= 20 or self.my_home.meal_cat <= 10:
            text = self.shop()
        elif self.my_home.money > 400:
            text = self.whife_goods()

        else:
            text = self.clean()

        print(self.name, text)
        return None

class Cat(Person):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.my_home = None

    def information(self):
        print(f'Name: {self.name}; Health: {self.health}; Meal: {self.my_home.meal_cat}.')

    def eat(self):
        if self.my_home.meal_cat > 0:
            n = self.my_home.meal_cat / 2  # add unknown parameter
            if n > 10:
                n = 10
                self.health += n * 2
                self.my_home.meal_cat -= n
            else:
                self.health += n * 2
                self.my_home.meal_cat -= n
            return 'is eating.'

    def sleep(self):
        self.health -= 5  # decided to reduce damage from life when he sleep
        return 'is sleeping.'

    def destroy(self):
        self.health -= 10
        self.my_home.dust += 5
        return 'is bad boy.'

    def one_day(self):
        dice = random.randint(1, 3)
        if self.health < 0:  # die
            return False
        if self.health < 20 and self.my_home.meal_cat >= 10:
            text = self.eat()
        elif dice == 1 or dice == 2:
            text = self.sleep()
        else:
            text = self.destroy()
        print(self.name, text)
        return None


home = House()
husband = Man('Tom', 30)
whife = Whife('Bob', 30)
cat = Cat('Begemot', 30)

husband.registration(home)
whife.registration(home)
cat.registration(home)

for day in range(1, 366):  # let's start
    print(f'\nDay: {day}')
    day_husband = husband.one_day()
    day_whife = whife.one_day()
    day_cat = cat.one_day()
    Man.information(husband)
    Whife.information(whife)
    Cat.information(cat)
    if day_husband == False:
        print('Tom - Husband is dead.')
        break
    if day_whife == False:
        print('Bob - Whife is dead.')
        break
    if day_cat == False:
        print('Cat is dead. Such a cruel world.')