#!/usr/bin/env python3
import random
import numpy

"""
Задание 1
Сформировать список из n точек на декартовой плоскости (х,у), заполнить значения координат точек случайными целыми числами (-100, 100).
Расположить точки в порядке обхода против часов стрелки, начиная с точки, ближайшей к оси у, лежащей в координатном углу I (положительные абсциссы и ординаты), если есть таковые. 
Найти среднее, мин., макс. расстояния точек от центра координатной плоскости (0,0). 
Вывести результаты на экран. 
Размер исходного списка n задается пользователем вручную после запуска программы.
"""

# функция расчета угла между осью абсцисс и точкой
def get_angle(point):
    anglePoint = numpy.arctan2(point[0], point[1])
    angle = numpy.arctan2(1, 0)
    return numpy.rad2deg((angle - anglePoint) % (2 * numpy.pi))    

pointNumber = input('Введите коичество точек ')
pointNumber = int(pointNumber)

# заполнение массива точек
# + определение максимально и минимально уделенных точек от начала коорлинат (0, 0)
# + сумма удаленности всех точек для расчета средней
pointArray = []
minRem = 100
maxRem = 0
sumRem = 0
for i in range(pointNumber):
    x = random.randint(-99, 99)
    y = random.randint(-99, 99)
    tmpRem = numpy.sqrt(numpy.power(x, 2)+numpy.power(y, 2))

    if tmpRem > maxRem:
        maxRem = tmpRem

    if tmpRem < minRem: 
        minRem = tmpRem

    sumRem += tmpRem    
    # print('x', x, 'y', y, 'rem', rem)
    pointArray.append([x, y ] * pointNumber)

# Вывод расстояния максимально и минимально удаленных точек
# Вывод среднего растояние
print('Минимальное растояние', minRem)
print('Максимальное растояние', maxRem)
print('Среднее растояние', (sumRem / pointNumber))

# сортировка точек с использованием функции получения угла
srt = sorted(pointArray, key=get_angle)

# вывод получившегося массива
print('Сортировка координат')
for i in range(len(srt)):
    print( "{} - ({},{}), угол={}".format((i + 1), srt[i][0], srt[i][1], get_angle(srt[i])) )    



    

