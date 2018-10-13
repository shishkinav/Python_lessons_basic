__author__ = 'Шишкин Анатолий'

# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

'''
Так получилось, что использую и дорабатываю код из hw5_normal.py так как уже большую часть задания этого уровня hard
уже реализовал.
'''
import lesson05.home_work.hw05_easy as my_modul
import sys, os


def print_help():
    '''
    функция выводи пользователю справку по доступным действиям
    '''
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cd <path_dir> - переход в директорию")
    print("rmdir <dir_name> - удаление директории в текущем каталоге")
    print("ls <path_dir> param - просмотр директории [параметры: file - отобразит только файлы указанной директории,"
          "dir - отобразит только папки указанной директории, all или оставьте параметр не заполненным - отобразит всё"
          "содержимое указанной директории]")
    print("cp <fileName> path pathFuture - копирует файл из директории в указанную директорию, если указать только"
          "имя файла, то копирование будет осуществляться в текущей директории где находится пользователь")
    print("rm <fileName - удаляет указанный файл из текущей директории")

def rmFile(nameFile):
    '''
    функция удаления файла
    '''
    try:
        os.remove(os.path.join(os.getcwd(), nameFile))
        print('файл удален')
    except FileNotFoundError:
        print('Такого файла не существует, проверьте имя файла')

# справочник действий по ключам пользователя
do = {
    "help": print_help,
    "mkdir": my_modul.addDir,
    "cd": my_modul.changeDir,
    "rmdir": my_modul.delDir,
    "ls": my_modul.seeCatalog,
    "cp": my_modul.copyFile,
    "rm": rmFile
}

# проверка третьего передаваемого параметра
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

# проверка второго передаваемого параметра
try:
    key = sys.argv[1]
except IndexError:
    key = None

# если ключ был передан, то получаем функцию по ключу
if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

do['cd']('..')
do['ls']('.')
do['cd']('home_work')
do['ls']('.')
do['cp']('copy_hw05_easy.py', '.')
do['rm']('copy_copy_hw05_easy')