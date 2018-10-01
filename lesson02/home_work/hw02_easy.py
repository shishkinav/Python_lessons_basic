__author__ = 'Шишкин Анатолий Васильевич'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
print('---Задача 1 - уровень easy - начало---')
fruits = ['яблоко', 'банан', 'киви', 'арбуз', 'абрикос', 'манго']
#перебираем каждый элемент списка и выводим его на экран с выравниманием
for fruit in fruits:
    print(fruits.index(fruit) + 1, '. {:>10}' .format(fruit))
print('---Задача 1 - уровень easy - завершение---')
input('Ознакомьтесь с результатом и нажмите Enter')

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
import random

print('---Задача 2 - уровень easy - начало---')
firstList = []
secondList = []
# заполняем первый список 20 элементами со значениями от 0 до 100
for number in range(20):
    firstList.append(random.randint(0, 100))
# заполняем второй список 10 элементами со значениями от 0 до 100
for number in range(10):
    secondList.append(random.randint(0, 100))

print('Мы работаем со следующими списками:\nfirstList = {}\nsecondList = {}' .format(firstList, secondList))

for element2 in secondList:                      # организуем перебор по каждому элементу второго списка
    for element1 in firstList:                  # перебираем все элементы первого списка
        if element1 == element2:        # проверяем совпадают ли элементы первого списка с проверяемым элементом второго списка на каждой итерации
            firstList.pop(firstList.index(element1))    # если обнаружено совпадение, то удаляем из первого списка элемент соответствующего индекса
print('В результате удаления из первого списка повторяющихся значений второго списка получим первый список вида:\n', firstList)
print('---Задача 2 - уровень easy - завершение---')
input('Ознакомьтесь с результатом и нажмите Enter')

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

#import random - в 3 задаче не делаю, так как во 2 задаче он уже подключен в этом файле

print('---Задача 3 - уровень easy - начало---')
list = []
# определяем рандомный список из 20 целых чисел
for number in range(20):
    list.append(random.randint(0, 100))
print('Сформированный список:\n', list)
# приступаем к шаманству над списком
for value in list:
    if value % 2 == 0:
        list[list.index(value)] = value / 4     # если кратно 2, то делим на 4 и подменяем текущее значение элемента в списке новым
    else:
        list[list.index(value)] = value * 2     # если не кратно 2, то умножаем на 2 и подменяем текущее значение элемента в списке новым
print('После обработки наш список примет вид:\n', list)

print('---Задача 3 - уровень easy - завершение---')
input('Ознакомьтесь с результатом и нажмите Enter')