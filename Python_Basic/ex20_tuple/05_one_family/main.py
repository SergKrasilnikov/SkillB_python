fam_dict = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Кононов', 'Ник'): 37,
    ('Кононова', 'Али'): 36,
    ('Кононов', 'Па'): 12
}

surname = input('Введите фамилию: ')
surname = surname.lower()

for i_person in fam_dict:
    if surname in i_person[0].lower() or surname + 'а' in i_person[0].lower() or surname[:len(surname) - 1] \
            in i_person[0].lower():
        print(i_person[0], i_person[1], fam_dict[i_person])