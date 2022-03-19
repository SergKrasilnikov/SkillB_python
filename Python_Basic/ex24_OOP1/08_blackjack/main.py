import random


class Man:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2


class Computer:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2


class Numbers:
    def number(self, add):
        # TODO, к переменной first_hand мы обратиться не можем внутри метода класса,
        #  т.к. переменная была создана вне класса.
        return first_hand + add


class Court:
    def number(self, add):
        # TODO, к переменной first_hand мы обратиться не можем внутри метода класса,
        #  т.к. переменная была создана вне класса.
        return first_hand + add


class Ace:
    def one_more_question(self):
        # TODO, к переменной first_hand мы обратиться не можем внутри метода класса,
        #  т.к. переменная была создана вне класса.
        question_ace = int(input('Ace is 1 or 11?'))
        if question_ace == 1:
            return first_hand + 1
        else:
            return first_hand + 11


while True:
    man = Man(random.randint(1, 11), random.randint(1, 11))  # 11 - Ace
    computer = Computer(random.randint(1, 11), random.randint(1, 11))  # 11 - Ace
    if man.card1 == 1:
        man.card1 = 10
    if man.card2 == 1:
        man.card2 = 10
    if computer.card1 == 1:
        computer.card1 = 10
    if computer.card2 == 1:
        computer.card2 = 10

    first_hand = man.card1 + man.card2
    computer_resalt = computer.card1 + computer.card2
    print(f'Cards: {man.card1} and {man.card2}. Summ: {first_hand}')

    while True:
        question = input('One more (y or n)?')
        if question == 'y':
            card = random.randint(1, 11)
            if card >= 2 and card <= 10:
                first_hand = Numbers.number(card)
            elif card == 1:  # 1 - Court
                card = 10
                first_hand = Court.number(card)
            else:
                first_hand = Ace.one_more_question(first_hand)
        else:
            man_result = first_hand
            break

    print(f'Computer results: {computer_resalt}')
    if man_result > computer_resalt:
        print('You win!\n')
    elif man_result == computer_resalt:
        print('No body win.\n')
    else:
        print('Computer win!\n')
