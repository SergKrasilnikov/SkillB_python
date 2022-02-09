print('Задача 8. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел

def calc(num1, num2):
  while num1 != 0 and num2 != 0:
      if num1 > num2:
          num1 = num1 % num2
      else:
          num2 = num2 % num1
  gcd = num1 + num2
  print(gcd)

while True:
  num1 = int(input('Введите первое число: '))
  num2 = int(input('Введите второе число: '))
  calc(num1, num2)