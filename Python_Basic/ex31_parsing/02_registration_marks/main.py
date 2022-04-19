import re

text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

private_template = r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}'
taxi_template = r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}'

list_new = re.findall(private_template and taxi_template, text)
print(list_new)

# COMMENT второй вариант
# import re
#
# text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
#
# list_new = re.findall(r'(?:\w\w\d\d\d\d\d\d)+' and r'(?:\w\w\d\d\d\d\d)+', text)
#
# print(list_new)