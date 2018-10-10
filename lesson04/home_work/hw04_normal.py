__author__ = 'Шишкин Анатолий Васиельвич'

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

import re

# как вариант через регулярку мы можем либо найти все рядом стоящие комбинации нижнего регистра, либо сплитануть по комбинациям верхнего регистра
f = re.findall(r'[a-z]+', line)
p = re.split(r'[A-Z]+', line)
# если надо вывести два результата уберите коммент print(f, 'длина - ', len(f), '\n', p, 'длина - ', len(f))

# реализация без применения re
value = ''
list_element = []
# перебираем все символы строки
for simbol in line:
    if simbol.islower():
        value += simbol     # при каждой итерации если символ маленький, то дописываем в спец переменную

    else:
        if value != '':     # если попадаем на большой символ, то проверяем не пуста ли спец переменная и если не пуста передаем её накопление в спец список, при этом обнуляем её
            list_element.append(value)
            value=''
if value != '':
    list_element.append(value)

print(list_element)
print(len(list_element))




# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
'''
использовал для проверок урывками
line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHB'
'''
line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

import re

listUpperSimbol = re.findall(r'[a-z]{2}([A-Z]+)[A-Z]{2}', line_2) # регулярка - это зверь
print(listUpperSimbol, 'длина списка с помощью регулярки - ', len(listUpperSimbol))

# теперь выполняем задачу муторно без регулярки
# решение мне подсказали, самостоятельно не разобрался (((, пришлось разбираться по чужому коду

countUpper = 0      # вводим переменную для подсчёта количества верхнерегистровых символов
listBig = []        # объявляем пустой список для хранения элементов

# запускаем перебор индексов исходной строки начиная с третьего символа
for indexElement in range(2, len(line_2)):
    # если символ строки с текущим индексом верхнеристровый и при этом если есть срез двух нижнерегистровых элементов подряд
    # срез line_2 [текущий индекс элемента - количество ранее найденных до этого верхнерегистровых элемента - 2 :
    # текущий индекс элемента - кол-во ранее найденных до этого верхнерегистровых элемента]. кол-во верхнерегистровых
    # используется для того, чтобы смешать срез влево на кол-во уже пройденных верхних символов и заодно считать их
    if line_2[indexElement].isupper() and line_2[indexElement - countUpper - 2 : indexElement - countUpper].islower():
        countUpper += 1
    # если мы дошли до этого условия, значит очередной элемент не является верхнерегистровым, проверяем набрано ли нужно количество верхнерегистровых
    elif countUpper <= 2:   # в данном случае не набрали нужного количества
        countUpper = 0      # обнуляем для следующей проверки
    elif countUpper > 2:    # а здесь набрали и передаём наш срез верхнерегистровых в список уменьшая срез на два символа справа
        listBig.append(line_2[indexElement - countUpper : indexElement - 2])
        countUpper = 0      # обнуляем для следующей проверки
# добавлено дублирование на случай, если кол-во индексов строки в цикле закончится, но не хватит итерации для проверки (если в конце исходной строки к примеру стоит три большие буквы
if countUpper > 2:
    listBig.append(line_2[indexElement - countUpper: indexElement - 2])

    '''
    моя наверное пятая переделка так и не удавшегося кода (((
for simbol in line_2:
    if simbol.islower():
        if len(value) > 2:
            listBig.append(value[:-2])
            countLower = 0
            value = ''
        elif line_2[(line_2.index(simbol) - 1)].isupper():
            countLower = 0
            value = ''
        else:
            value = ''

        countLower += 1
    elif simbol.isupper():
        if countLower < 2:
            countLower = 0
            value = ''
        else:
            value += simbol
'''

print(listBig, 'длина списка без использования регулярки - ', len(listBig))



# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
