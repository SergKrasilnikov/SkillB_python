class Parent:
    def __init__(self, name, age, ch_list):
        self.name = name
        self.age = age
        self.ch_list = []
        self.is_it_your_child(ch_list)

    def is_it_your_child(self, child_list):
        for child in child_list:
            if self.age - child.age >= 16:
                self.ch_list.append(child)
            else:
                print(f'{child.name} is not my baby!')

    def information(self):
        print(f'My name {self.name}, I am {self.age} years old.')
        for child in self.ch_list:
            print(f'I have {child.name} in my life.')

    def take_care(self):
        for person in self.ch_list:
            if person != 'ok':
                person.condition = 'ok'

    def give_something(self):
        for person in self.ch_list:
            if person != 'full':
                person.energy = 'full'


class Child:
    def __init__(self, name, age, condition, energy):
        self.name = name
        self.age = age
        self.condition = condition
        self.energy = energy

    def information(self):
        print(f'Name: {self.name}. Age: {self.age}. Condition: {self.condition}. Energy: {self.energy}')


marry = Child('Marry', 15, 'ok', 'full')
adam = Child('Adam', 3, 'hot', 'low')
parent = Parent('Bob', 25, [marry, adam])
parent.information()

marry.information()
adam.information()

parent.take_care()
adam.information()

parent.give_something()
adam.information()

# зачёт!
