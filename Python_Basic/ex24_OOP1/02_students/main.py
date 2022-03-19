import random


class Student:
    def __init__(self, name, gang, sex, age):
        self.name = name
        self.gang = gang
        self.grade = 0
        self.sex = sex
        self.age = age
        self.average_value()

    def __repr__(self):
        return f'{self.name}-{self.gang}-{round(self.grade)}-{self.sex}-{self.age}'

    def average_value(self):
        for _ in range(5):
            self.grade += random.randint(0, 100)
        self.grade = self.grade / 5

    def get_average_age(self):
        return self.grade


St_1 = Student('Tom', 1, 'M', random.randint(18, 100))
St_2 = Student('Bob', 1, 'M', random.randint(18, 100))
St_3 = Student('Den', 1, 'M', random.randint(18, 100))
St_4 = Student('Jane', 1, 'F', random.randint(18, 100))
St_5 = Student('Main', 1, 'F', random.randint(18, 100))
St_6 = Student('Kevin', 2, 'M', random.randint(18, 100))
St_7 = Student('Elvis', 2, 'M', random.randint(18, 100))
St_8 = Student('Jennifer', 2, 'F', random.randint(18, 100))
St_9 = Student('Lilu', 2, 'F', random.randint(18, 100))
St_10 = Student('Megan', 2, 'F', random.randint(18, 100))

people = [St_1, St_2, St_3, St_4, St_5, St_6, St_7, St_8, St_9, St_10]

people.sort(key=lambda x: x.get_average_age(), reverse=True)

for sorted_i in people:
    print(sorted_i)

# зачёт!
