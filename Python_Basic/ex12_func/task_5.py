print('Задача 5. Текстовый редактор')

# Напишите функцию count_letters,
# которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
#
# Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определенном формате.
#
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищём? л
#
# Количество цифр 0: 2
# Количество букв л: 1

def count_letters(text, num, letter):
  count_n = 0
  count_l = 0
  for count in text:
    if count == num:
      count_n += 1
    elif count == letter:
      count_l += 1

  print('Количество цифр ' + num + ': ' + str(count_n))
  print('Количество букв ' + letter + ': ' + str(count_l) + '\n')



while True:
  text = input('Введите текст: ')
  num = input('Какую цифру ищем? ')
  letter = input('Какую букву ищём? ')
  count_letters(text, num, letter)