__author__ = 'Шишкин Анатолий Васильевич'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
# 1 1 2 3 5 8 13

def fibonacci(n, m):
    '''
    функция выводит на печать участок ряда фибоначи с элемента n по элемент m
    '''
    fb = []
    '''
    # через цикл формируем ряд фибоначчи вплоть до элемента m, запрошенного пользователем
    for i in range(m):
        if 0 <= i <= 1:
            fb.append(1)
        else:
            fb.append(fb[i-2] + fb[i-1])
    # делаем возврат из функции запрашиваемого ряда fb
    return print('Запрашиваемый вами участок ряда фибоначи выглядит следующим образом:\n', fb[n:m])

print('--- Задача 1 - уровень normal - начало ---')

# запрашиваем у пользователя начальный и конечный элементы для вывода и радуемся
fibonacci(int(input('Введите начало участка ряда Фибоначчи:\n')), int(input('Введите окончание интересующего участка ряда Фибоначчи:\n')))

print('--- Задача 1 - уровень normal - конец ---')
input('Посмотрите результат и нажмите Enter')
'''
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    '''
    функция сортирует элементы списка по возрастанию
    '''
    current_list = []       # создаем промежуточный список
    # запускаем количество итераций по проходу количества элементов списка
    print('Исходный список:\n', origin_list)
    for i in range(len(origin_list)):
        minElement = origin_list[0]                 # утверждаем, что первый элемент списка является минимальным
        # перебираем все оставшиеся элементы списка и сравниваем с минимальным
        for element in origin_list:
            if minElement >= element:   # если находим элемент меньше либо равный минимальному, то забираем его значение и запоминаем его индекс
                minElement = element
                index = origin_list.index(element)
        origin_list.pop(index)          # после прохождения цикла по всем элементам мы точно знаем индекс и значение самого минимального, поэтому удаляем его из списка, а его значение передаём в новый список
        current_list.append(minElement)
    return print('Отсортированный список\n', current_list)          #печатаем получившийся промежуточный список

print('--- Задача 2 - уровень normal - конец ---')

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

print('--- Задача 2 - уровень normal - конец ---')
input('Посмотрите результат и нажмите Enter')

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

print('--- Задача 3 - уровень normal - начало ---')

def myFilter(fun, list):
    '''
    принцип действия функции схож с filter, только она при этом не отдельные элементы возвращает, а сразу отфильтрованный список
    '''
    currentList = []
    # перебираем все элементы полученного списка
    for elementList in list:
        # если полученная в качестве параметра функция от элемента возвращает True, то он попадает в отфильтрованный список
        if fun(elementList):
            currentList.append(elementList)
    # возвращаем отфильтрованный список
    return currentList

print(myFilter(len, ['', 'sdf', '234']))            # вернёт только два последних элемента
print(myFilter(lambda x: x-10 > 0, [1, 10, 20]))    # вернёт только 20

print('--- Задача 3 - уровень normal - конец ---')
input('Посмотрите результат и нажмите Enter')

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

