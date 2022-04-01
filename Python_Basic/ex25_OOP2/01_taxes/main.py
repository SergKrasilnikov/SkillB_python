class Property:
    def __init__(self, worth):
        self.worth = worth
        self.persent = 1

    def taxes(self):
        return self.worth / self.persent

class Appartment(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.persent = 1000

class Car(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.persent = 200

class CountryHouse(Property):

    def __init__(self, worth):
        super().__init__(worth)
        self.persent = 500

while True:
    money = int(input('Amount of money: '))
    appartment_price = int(input('The price of appartment: '))
    car_price = int(input('The car price: '))
    country_price = int(input('The price of country house: '))

    appartment = Appartment(appartment_price)
    car = Car(car_price)
    country = CountryHouse(country_price)

    if money > (appartment.taxes() + car.taxes() + country.taxes()):
        taxes = appartment.taxes() + car.taxes() + country.taxes()
        print(f'You have {taxes} taxes in this year.')
    else:
        print(f"You don't have enough money to pay for your shit. You need {taxes - money} more.")