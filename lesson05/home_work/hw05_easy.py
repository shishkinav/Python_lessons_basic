__author__ = 'Шишкин Анатолий'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os, re

def addDir(nameDir):
    '''
    функция создаёт в текущей директории папку с передаваемым именем
    '''
    dirPath = os.path.join(os.getcwd(), nameDir)
    try:
        os.mkdir(dirPath)
        print('директория {} создана'.format(nameDir))
    except FileExistsError:
        print('директория {} существует' .format(nameDir))

def delDir(nameDir):
    '''
    функция удаляет из текущей директории папку с передаваемым именем
    '''
    dirPath = os.path.join(os.getcwd(), nameDir)
    try:
        os.rmdir(dirPath)
        print('директория {} удалена'.format(nameDir))
    except FileExistsError:
        print('директории {} не существует' .format(nameDir))

# весь этот блок ниже не будет доступен при импорте этого файла в качестве модуля
if __name__ == "__main__":
    while True:
        change = input('[1] создать директории\n[2] удалить директории\n'
                       '[3] выйти из программы\nВыберите номер действия:\n')
        if change == '1':   # команда создания
            for i in range(9):
                addDir('dir_' + str(i + 1))
        elif change == '2': # команда удаления
            for i in range(9):
                delDir('dir_' + str(i + 1))
        elif change == '3': # команда выхода
            break
        else:               # некорректный номер ввода
            print('номер действия введен неправильно')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def seeCatalog (path, param):
    '''
    функция выводит пользователю содержимое каталога, находящегося по адресу path, в зависимости от параметра
    'file' - отобразит только файлы
    'dir' - отобразит только папки
    'all' - отобразит всё содержимое текущего каталога
    '''
    if param == 'file':
        print([el for el in os.listdir(path) if re.search('[.]+\w+', el)])
    elif param == 'dir':
        print([el for el in os.listdir(path) if not re.search('[.]+\w+', el)])
    elif param == 'all':
        print([el for el in os.listdir(path)])
    else:
        print('указан неверный параметр для отображения (используйте file, dir или all')

seeCatalog(os.getcwd(), 'file')
seeCatalog(os.getcwd(), 'dir')
seeCatalog(os.getcwd(), 'all')

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
