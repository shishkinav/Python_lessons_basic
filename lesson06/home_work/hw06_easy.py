# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from math import sqrt


def checkValue(value):
    '''
    функция проверки корректности задаваемой координаты
    '''
    try:
        return float(value) # если нормально преобразуется во float, то возвращаем его
    except ValueError:
        print('значение введено некорректно') # если ошибка, то пишем о некорректности и возвращаем None
        return None

def EnterValue(countVertex):
    '''
    функция автоматизации ввода координат точки
    '''
    while True:
        x = round(checkValue(input('Введите значение координаты х для {} вершины:\n' .format(countVertex))), 2)
        y = round(checkValue(input('Введите значение координаты y для {} вершины:\n'.format(countVertex))), 2)
        if x != None and y != None:
            return (x, y)


class Triangle():
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        # производим расчёт длин отрезков и передаём их в формате справочника
        self.lenVector = {
                'a': round(sqrt((self.point1[0] - self.point2[0]) ** 2 + (self.point1[1] - self.point2[1]) ** 2), 2),
                'b': round(sqrt((self.point2[0] - self.point3[0]) ** 2 + (self.point2[1] - self.point3[1]) ** 2), 2),
                'c': round(sqrt((self.point1[0] - self.point3[0]) ** 2 + (self.point1[1] - self.point3[1]) ** 2), 2)
                }

    def calculateHeight(self):
        '''
        уникальный метод для Triangle по расчёту высоты
        '''
        p = 1 / 2 * (self.lenVector['a'] + self.lenVector['b'] + self.lenVector['c'])
        return round((2 * sqrt(p * (p - self.lenVector['a']) * (p - self.lenVector['b']) * (p - self.lenVector['c']))) / self.lenVector['a'], 2)

    def squareFigure(self):
        '''
        метод рассчитывает площадь фигуры зная высоту height и основание, либо сумму оснований base фигуры
        '''
        return round(1 / 2 * self.lenVector['a'] * self.calculateHeight(), 2)

    def Perimetr(self):
        '''
        метод рассчитывает перимет, получая список длин всех сторон многоугольника
        '''

        return self.lenVector['a'] + self.lenVector['b'] + self.lenVector['c']

# раскоментировать если хотим самостоятельно вводить все координаты
# test = Triangle(EnterValue(1), EnterValue(2), EnterValue(3))
test = Triangle((0, 0), (4, 4), (4, 0))

print('Периметр треугольника - %r условных единиц' % test.Perimetr())
print('Высота треугольника   - %r условных единиц' % test.calculateHeight())
print('Площадь треугольника  - %r условных единиц в квадрате' % test.squareFigure())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

# создаём класс трапеций, наследуя методы и атрибуты из класса треугольник
class Trapec (Triangle):
    # конструктор класса трапеции
    def __init__(self, point1, point2, point3, point4):
        # вызов конструктора из суперкласса
        Triangle.__init__(self, point1, point2, point3)
        # определяем уникальный атрибут класса
        self.point4 = point4

        # обновляем расчёт длины 'c' и добавляем длину 'd' и корректируем с передачей данные в справочник
        self.lenVector.update({'c': round(sqrt((self.point3[0] - self.point4[0]) ** 2 + (self.point3[1] - self.point4[1]) ** 2), 2)})
        self.lenVector.update({'d': round(sqrt((self.point1[0] - self.point4[0]) ** 2 + (self.point1[1] - self.point4[1]) ** 2), 2)})

    def checkTrap(self):
        '''
        проверка трапеции на равнобедренность
        '''
        if self.lenVector['a'] == self.lenVector['c'] or self.lenVector['b'] == self.lenVector['d']:
            return True
        else:
            return False

    # переопределяем метод по расчёту высоты
    def calculateHeight(self):
        '''
        метод Трапеции для расчёта высоты
        '''
        return round(sqrt(self.lenVector['a'] ** 2 - (self.lenVector['d'] - self.lenVector['b']) ** 2 / 4), 2)

# раскоментировать если хотим самостоятельно вводить все координаты трапеции
# manyAngle = Trapec(EnterValue(1), EnterValue(2), EnterValue(3), EnterValue(4))
manyAngle = Trapec((0, 0), (1, 2), (4, 2), (5, 0))
# проверяем равнобедренная ли трапеция и если нет, то расчёт не будет проводиться
if manyAngle.checkTrap():
    print('\n\nЗадана Трапеция:')
    for i in '1234':
        print(i, ' вершина с координатами ', eval('manyAngle.point' + i))
    for simbol in 'abcd':
        print('Длина стороны {} в трапеции - {} условных единиц' .format(simbol, manyAngle.lenVector[simbol]))
    print('Периметр трапеции   - %r условных единиц' % (manyAngle.Perimetr() + manyAngle.lenVector['d']))
    print('Площадь трапеции  - %r условных единиц в квадрате' % test.squareFigure())
else:
    print('Ваша трапеция не равнобедренная и не подлежит решению в данном коде')