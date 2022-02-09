print('Задача 7. Стипендия')

#Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
#
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.

educational_grant = int(input('Ежемесячная стипендия студента составляет, руб.: '))
educational_grant *= 10
print(educational_grant)
parents_money = month = 0
expenses = int(input('Расходы на проживание, руб.: '))
for months_list in range(1, 10): #за 2 - 10 месяц обучения
  print('месяц', months_list)
  expenses += (expenses * 3) / 100
  month += expenses
month += 12000 #за первый месяц обучения
if educational_grant < month:
  parents_money = month - educational_grant
print('У родителей нужно взять: ', parents_money)