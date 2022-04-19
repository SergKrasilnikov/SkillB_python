import re

list_text = ['9999999999', '999999-999', '99999x9999']
count = 0

for unit in list_text:
    count += 1
    if re.match(r'[8-9]{1}[0-9]{9}', unit) and len(unit) == 10:
        print(f'Phone number {count}: is valid')
    else:
        print(f'Phone number {count}: uncorrect')