#!/usr/bin/env python3
import re

"""
Задание 2
Написать программу на языке python версии 3, отсеивающую автомобильные номера неправильного формата, т.е. проверка ГРЗ типа 1А из проверочного списка. 
Пример списка: ["A123AA11", "А222АА123", "A12AA123", "A123CC1234", "AA123A12"].
Для данного примера правильным ответом будет  ["A123AA11", "А222АА123"]. 
Дополнить список верными и неверными номерами. Список для проверки в теле программы (не в файле).
"""

# строка с перечислением гос.номеров
numbersStr = 'А123АА11,CC333А12,АА12А123,А111АА22,А222АА123,А12АА123,А123СС1234,АА123А12,С123СС1,ААА123С,А333АА12'

# функция проверки соответствия гос.номера типу 1А
def filter_1a(num):
    if ( re.match(r'^(А{1}\d{3}А{2}\d{1,3})$', num) ):
        return True
    else:
        return False

# получение массива из строки-перечисления гос.номеров
numArray = numbersStr.split(',')

# получение списка номеров, соответствующих типу 1Аы
correctNumArray = list(filter(filter_1a, numArray))

# вывод корректного списка
print('Список корректных ГРЗ 1А')
for i in range(len(correctNumArray)):
    print(correctNumArray[i])
    