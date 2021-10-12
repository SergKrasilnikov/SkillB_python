print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

text = input('Введите числа через пробел: ')
num = max_num = 0
str_max = temp_str = ''

for num_count in text:
  if num_count == ' ':
    if num > max_num:
      max_num = num
      str_max = temp_str
    num = 0
    temp_str = ''
    continue
  num += int(num_count)
  temp_str += num_count
if num > max_num:
  max_num = num
  str_max = temp_str

print('Число с максимальной суммой:', str_max, 'Сумма цифр этого числа:', max_num)