__author__ = 'Шишкин Анатолий Васильевич'

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
import random
import math

print('\n---Задача 1 - уровень normal - начало---\n')
list1 = []
list2 = []
# определяем рандомный список из 20 целых положительных или отрицательных чисел
for number in range(20):
    list1.append(random.randint(-50, 100))
print('Сформированный список:\n', list1)

# собственно этими тремя строчками мы проверяем весь список и при выполнении волшебных условий наполняем второй список значениями
for element in list1:
    if (element >= 0) and (math.sqrt(element) % 1 == 0):
        list2.append(int(math.sqrt(element)))
print('Мы обработали список\n{}\nи получили из него следующий список\n{}' .format(list1, list2))
print('\n---Задача 1 - уровень normal - завершение---\n')
input('Ознакомьтесь с результатом и нажмите Enter')

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

print('\n---Задача 2 - уровень normal - начало---\n')
# создаём справочники значений числа и месяца
date = {'01':'первое', '02':'второе', '03':'третье', '04':'четвертое', '05':'пятое', '06':'шестое', '07':'седьмое',
    '08':'восьмое', '09':"девятое", '10':'десятое', '11':'одиннадцатое', '12':'двенадцатое', '13':'тринадцатое', '14':'четырнадцатое',
    '15':'пятнадцатое', '16':'шестнадцатое', '17':'семьнадцатое', '18':'восемьнадцатое', '19':'девятнадцатое', '20':'двадцатое',
    '21':'двадцать первое', '22':'двадцать второе', '23':'двадцать третье', '24':'двадцать четвертое', '25':'двадцать пятое',
    '26':'двадцать шестое', '27':'двадцать седьмое', '28':'двадцать восьмое', '29':'двадцать девятое', '30':'тридцатое', '31':'тридцать первое'}
month = {'01':'января', '02':'февраля', '03':'марта', '04':'апреля', '05':'мая', '06':'июня', '07':'июля',
    '08':'августа', '09':'сентября', '10':'октября', '11':'ноября', '12':'декабря'}

# запрашиваем от пользователя дату в определенном формате
userDate = input('Введите дату в формате DD.MM.YYYY: ')
# используем слайсы и имеющиеся справочники, чтобы преобразовать цифры в текстовые значения
print('На портале времени вы выбрали для телепортации дату - {} {} {} года' .format(date[userDate[0:2]], month[userDate[3:5]], userDate[6:] ))

print('\n---Задача 2 - уровень normal - завершение---\n')
input('Ознакомьтесь с результатом и нажмите Enter')

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

print('\n---Задача 3 - уровень normal - начало---\n')

n = int(input('Какое количество элементов вы хотите увидеть в списке (введите целое число): '))
list = []
for element in range(n):
    list.append(random.randint(-100, 100))
print('Вы запросили список с количеством элементов {}\nв результате получился список\nlist = {}' .format(n, list))

print('\n---Задача 3 - уровень normal - завершение---\n')
input('Ознакомьтесь с результатом и нажмите Enter')

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
