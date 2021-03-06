
__author__ = 'Шишкин Анатолий Васильевич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

print('--- Начало первой задачки ---')
while True:     # зацикливание программы пока пользователь сам не изъявит желения выйти
    sourceNumber = input('Введите произвольное целое число, или введите "Q" для выхода из программы: ')
    if sourceNumber == 'Q' or sourceNumber == 'q':
        print('Вы остановили исполнение программы.')
        break
    sourceNumber = int(sourceNumber)
    number = sourceNumber // 10
    maxNumber = sourceNumber % 10 #предполагаем в начале программы, что последняя цифра введенного числа самая большая
    while True:
        if maxNumber < (number % 10):
            maxNumber = number % 10     #если окажется, что уже присвоенное значение меньше проверяемого, то запоминаем новое максимальное
        elif number // 10 == 0:
            break
        number = number // 10           #готовимся к новой итерации, поэтому отбрасываем уже проверенную цифру

    print('Максимальная цифра в данном числе - ', maxNumber)
print('--- Конец первой задачки ---')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print('--- Начало второй задачки ---')
print('Вариант 1. Обмен значениями между двух переменных через действия с числами')
variable_1 = int(input('Введите значение первой переменной: '))
variable_2 = int(input('Введите значение второй переменной: '))
variable_1 = variable_1 + variable_2 #присваеваем одной из переменных их сумму
variable_2 = variable_1 - variable_2 #присваеваем второй переменной измененное значение полученное через разницу суммы и известного значния второй переменной
variable_1 = variable_1 - variable_2 #присваеваем первой переменной измененное значение, полученное через разницу суммы и известного значения первой переменной
print('Программа произвела замену и теперь в первой переменной лежит значение: ', variable_1, ', а во второй переменной лежит значение: ', variable_2)
input('Ознакомьтесь с результатом и нажмите Enter для закрытия второй задачи')

print('Вариант 2. Обмен значениями между двух переменных с использованием кортежа')
variable_1 = int(input('Введите значение первой переменной: '))
variable_2 = int(input('Введите значение второй переменной: '))
variable_1, variable_2 = variable_2, variable_1 #проводим change
print('Программа произвела замену и теперь в первой переменной лежит значение: ', variable_1, ', а во второй переменной лежит значение: ', variable_2)
input('Ознакомьтесь с результатом и нажмите Enter для закрытия второй задачи')
print('--- Конец второй задачки ---')


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print('--- Начало третьей задачки ---')
import math

print('Сегодня мы с вами решим квадратное уравнение.\nВспоминаем как оно выглядит)) ax² + bx + c = 0\nВспомнили, теперь поехали...')
a = int(input('Введите значение коэффициента а: '))
b = int(input('Введите значение коэффициента b: '))
c = int(input('Введите значение коэффициента c: '))
D = b**2 - 4 * a * c
print('D = ', D)
if D > 0:
    x1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print('Корни квадратного уравнения следующие:\n x1 = ', x1, '\n x2 = ', x2)
elif D == 0:
    x1 = x2 = (-b) / (2 * a)
    print('Корни квадратного уравнения x1 = x2 = ', x1)
else:
    print('Для квадратного уравнения с введенными вами коэффициентами a = ', a, ' b = ', b, ' c = ', c, '\nРешений не существует.')
input('Пожалуйста, ознакомьтесь с результатом вычислений и нажмите клавишу Enter')
print('--- Конец третьей задачки ---')
