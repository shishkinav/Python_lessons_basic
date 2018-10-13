__author__ = 'Шишкин Анатолий'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os, re, shutil

def changeDir(path):
    '''
    функция осуществляет переход в указанную директорию
    '''
    try:
        os.chdir(path)
        print('переход совершен успешно')
    except FileNotFoundError:
        print('переход невозможен, такая директорая не существует')

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

def seeCatalog (path = '.', param = None):
    '''
    функция выводит пользователю содержимое каталога, находящегося по адресу path, в зависимости от параметра
    'file' - отобразит только файлы
    'dir' - отобразит только папки
    'all' - отобразит всё содержимое текущего каталога
    '''
    # если для просмотра каталога параметр не передан, то по умолчанию будет отображено всё содержимое папки
    if param == None:
        param = 'all'
    try:
        if param == 'file':
            print([el for el in os.listdir(path) if re.search('[.]+\w+', el)])
        elif param == 'dir':
            print([el for el in os.listdir(path) if not re.search('[.]+\w+', el)])
        elif param == 'all':
            print([el for el in os.listdir(path)])
        else:
            print('указан неверный параметр для отображения (используйте file, dir или all')
    except FileNotFoundError:
        print('введенной вами директории не существует')

# чтобы не импортировалось в другие файлы
if __name__ == "__main__":
    seeCatalog(os.getcwd(), 'file')
    seeCatalog(os.getcwd(), 'dir')
    seeCatalog(os.getcwd(), 'all')

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copyFile(nameFile, path, pathFuture = None):
    '''
    функция копирует файл из директории path (в скрипте своём можете использовать os.getcwd()) в директорию pathFuture
    (если копируете файл в ту же директорию, то оставьте третий параметр пустым), в качестве второго параметра
    передавайте только имя файла, который хотите скопировать (для передачи имени открытого скрипта используйте
    в своём скрипте os.path.basename(__file__), либо указывайте имя файла другими доступными способами
    '''
    try:
        # если третий параметр не передавался, то мы передаём ему значение той же директории
        if pathFuture == None:
            pathFuture = path
        # копируем файл комбинируя кросплатформенно пути и добавляя к имени в начале текст 'copy_'
        shutil.copy(os.path.join(path, nameFile), os.path.join(pathFuture, 'copy_' + nameFile))
        print('файл с именем {} скопирован в директорию {}' .format(nameFile, pathFuture))
    except FileNotFoundError:
        print('проверьте путь и имя файла - таких не существует')

# далее код будет работать, только если мы будем запускать этот скрипт, при импортировании ниже строчки не сработают
#if __name__ == "__main__":
#    copyFile(os.getcwd(), os.path.basename(__file__), '../examples/my_libs/')   # скопирует открытый файл в новую папку
#    copyFile(os.getcwd(), os.path.basename(__file__))                          # скопирует открытый файл в ту же папку
#    copyFile(os.getcwd(), 'file')                                               # скажет об отсутствии такого файла
