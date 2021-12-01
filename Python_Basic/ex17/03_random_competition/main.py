import random

winners = []  # Возможно, строка кода получилась лишней, т.к. переменная создаётся в коде ниже.

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [(first_team[slot] if first_team[slot] >= second_team[slot] else second_team[slot])
           for slot in range(20)]

print('Первая команда', first_team)
print('Вторая команда', second_team)
print('Победители турнира:', winners)