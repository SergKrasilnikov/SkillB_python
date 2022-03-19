class Potato:
    states = {0: 'Empty', 1: 'Sprout', 2: 'Green', 3: 'Ready'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f'Patato {self.index} have {Potato.states[self.state]} state.')


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Potato grow old.')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Potato is not ready.\n')
        else:
            print('All potato is ready.')


class Gardener:
    def __init__(self, name, collected, my_garden):
        self.name = name
        self.collected = collected
        self.my_garden = my_garden

    def info(self):
        print(f'Name of gardener: {self.name}. Collected potato: {self.collected}.')

    def take_care(self):
        self.my_garden.grow_all()
        self.my_garden.are_all_ripe()

    def grab_potatoes(self):
        if all([i_potato.is_ripe() for i_potato in self.my_garden.potatoes]):
            for i_potato in self.my_garden.potatoes:
                self.collected += 1
                i_potato.state = 0


my_garden = PotatoGarden(5)
my_gardener = Gardener('Bob', 0, my_garden)

print(my_gardener.info())
for _ in range(3):
    my_gardener.take_care()
my_gardener.grab_potatoes()
print(my_gardener.info())

#  В текущем задании, нам необходимо реализовать наш код таким образом, чтобы в основном коде были обращения
#  только к методам нашего садовника.
#  Садовник внутри своих методов, может обращаться к методам Грядки, т.к. Грядка является аргументом класса Садовник.
#  А Грядка, внутри своих методов, может обращаться к методам Картошки, т.к. список элементов Картошка, является
#  аргументом класса Грядка.
#  В итоге, при помощи методов Садовника, мы должны:
#  1. Посадить урожай на Грядке.
#  2. Ухаживать за грядкой.
#  3. Проверять состояние грядки.
#  4. Собирать урожай на грядке.


# COMMENT тоже работет

# class Potato:
#     states = {0: 'Empty', 1: 'Sprout', 2: 'Green', 3: 'Ready'}
#
#     def __init__(self, index):
#         self.index = index
#         self.state = 0
#
#     def grow(self):
#         if self.state < 3:
#             self.state += 1
#         self.print_state()
#
#     def is_ripe(self):
#         if self.state == 3:
#             return True
#         return False
#
#     def print_state(self):
#         print(f'Patato {self.index} have {Potato.states[self.state]} state.')
#
# class PotatoGarden:
#     def __init__(self, count):
#         self.potatoes = [Potato(index) for index in range(1, count + 1)]
#
#     def grow_all(self):
#         print('Potato grow old.')
#         for i_potato in self.potatoes:
#             i_potato.grow()
#
#     def are_all_ripe(self):
#         if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
#             print('Potato is not ready.\n')
#         else:
#             print('All potato is ready.')
#
# class Gardener:
#     def __init__(self, name, collected):
#         self.name = name
#         self.collected = collected
#
#     def info(self):
#         print(f'Name of gardener: {self.name}. Collected potato: {self.collected}.')
#
#     def take_care(my_gardener, my_garden):
#         my_garden.grow_all()
#         my_garden.are_all_ripe()
#
#     def grab_potatoes(self):
#         if all([i_potato.is_ripe() for i_potato in my_garden.potatoes]):
#             for i_potato in my_garden.potatoes:
#                 my_gardener.collected += 1
#                 i_potato.state = 0
#
# my_garden = PotatoGarden(5)
# my_gardener = Gardener('Bob', 0)
#
# print(my_gardener.info())
# for _ in range(3):
#     my_gardener.take_care(my_garden)
# my_gardener.grab_potatoes()
# print(my_gardener.info())

# зачёт!
