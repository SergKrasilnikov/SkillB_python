class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __repr__(self):
        return f'{self.__name}-{self.__surname}'

class Employee(Person):
    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname, age)
        self.salary = salary

    def salary_count(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age, salary=13000)

    def salary_count(self):
        return self.salary

class Agent(Employee):
    def __init__(self, name, surname, age, sells):
        super().__init__(name, surname, age, salary=5000)
        self.sells = sells

    def salary_count(self):
        return self.salary + (self.sells * 5 / 100)

class Worker(Employee):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age, salary=100)
        self.hours = hours

    def salary_count(self):
        return 100 * self.hours

manager_1 = Manager('Bill', 'Bil', 25)
manager_2 = Manager('Tomm', 'Tom', 26)
manager_3 = Manager('Jenn', 'Jen', 27)
agent_1 = Agent('Fill', 'Fil', 25, 100000)
agent_2 = Agent('Mill', 'Mil', 26, 110000)
agent_3 = Agent('Dill', 'Dil', 27, 150000)
worker_1 = Agent('Dann', 'Dan', 25, 80)
worker_2 = Agent('Pann', 'Pan', 26, 85)
worker_3 = Agent('Funn', 'Fun', 27, 82)

people = [manager_1, manager_2, manager_3, agent_1, agent_2, agent_3, worker_1, worker_2, worker_3]

for i_person in people:
    print(f'Employee: {i_person} - {i_person.salary_count()}')