
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""

import requests, os, re, datetime
import json, sqlite3

baseName = 'weather.sqlite' # глобальная переменная с названием базы данных

def listCountry():
    '''
    функция возврата уникальных кодов стран по имеющимся в локальной базе городам
    '''
    try:
        with sqlite3.connect(baseName) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("select * from weather")
            listCnt = []
            for row in cur.fetchall():
                idCity, city, country, date, temperature, idWeather = row
                listCnt.append(country)
            return set(listCnt)
    except sqlite3.OperationalError:
        createBase()
        listCountry()

# инициировать проверку idCity на наличие в базе данных
def parsCityListJson():
    '''
    функция парсит исходный JSON файл со списком городов, проверяет есть ли такие города в локальной базе и
    если нет, то актуализирует сведения и дописывает в базу
    '''
    path = os.path.join('lib', 'city.list.json')
    with open(path, 'r', encoding='UTF-8') as file:
        with sqlite3.connect(baseName) as conn:
            try:
                result = json.loads(file.read())
                tempListLocalId = listLocalID()
                for stroka in result:
                    if stroka['id'] in tempListLocalId:
                        print('Id существует')
                        continue
                    else:
                        try:
                            el = requestIdTown(stroka['id'])
                            # Записываем новые данные в локальную базу
                            conn.execute("""
                                                insert into weather (idCity, city, country, date, temperature, idWeather) VALUES (?,?,?,?,?,?)""",
                                         (
                                             stroka['id'],
                                             stroka['name'],
                                             stroka['country'],
                                             datetime.date.today(),
                                             el[0],
                                             el[1]
                                         )
                                         )
                            # информируем пользователя, что запись создана
                            print('добавлена строка', stroka['id'], stroka['name'], stroka['country'], datetime.date.today(), el[0], el[1])

                        except TypeError:
                            pass
            except sqlite3.IntegrityError:
                pass
            except sqlite3.OperationalError:
                createBase()


def requestIdTown(id = 707860): # 5601538 - Москва
    '''
    функция, получая id города, отправляет запрос на API и после получения возвращает данные температуры и кода погоды
    '''
    try:
        s=requests.get('http://api.openweathermap.org/data/2.5/weather?id='+ str(id) + '&units=metric&appid=52773c4f40a2d698eb8ea071bece011a')
        data = json.loads(s.text)

        return data['main']['temp'], data['weather'][0]['id']
    except:
        print('Ошибка запроса данных по API для idCity = ', id)

def createBase(baseName = baseName):
    # Указываем название файла базы данных
    try:
        conn = sqlite3.connect(baseName)
        # Создаем схемы в базе данных
        with sqlite3.connect(baseName) as conn:
            conn.execute('''
                create table weather (
                    idCity      integer primary key,
                    city        varchar(255),
                    country     varchar(255),
                    date        date,
                    temperature integer,
                    idWeather  integer
                );
                ''')
    except sqlite3.OperationalError:
        print('База данных с таким именем уже создана')



def viewValueBase(param = None, baseName = baseName):
    '''
    Функция обращения к локальной базе данных для просмотра данных по запросу.
     param = 'all' - отобразит всю локальную базу значений
     param = '<country>' - отобразит записи по введенной стране, например, 'RU' - увидим все города России из базы
    '''
    try:
        with sqlite3.connect(baseName) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("select * from weather")
            print('{:<10}{:<50}{:<10}{:<17}{:<15}{:<15}'.format('id_города', 'Город', 'Страна', 'Обновлялось',
                                                                'Температура', 'id_погоды'))
            for row in cur.fetchall():
                idCity, city, country, date, temperature, idWeather = row
                if param == 'all':
                    print('{:<10}{:<50}{:<10}{:<17}{:<15}{:<15}'.format(idCity, city, country, date, temperature,
                                                                        idWeather))
                elif str(country) == param:
                    print('{:<10}{:<50}{:<10}{:<17}{:<15}{:<15}'.format(idCity, city, country, date, temperature,
                                                                        idWeather))
                else:
                    print('Параметер не был указан')

    except sqlite3.OperationalError:
        createBase()
        viewValueBase()

def updateValueBase(idCity, date, temperature, baseName = baseName):
    '''
    функция обновляет значение температуры и меняет дату обновления в записи локальной базы по id города
    '''
    with sqlite3.connect(baseName) as conn:
        cur = conn.cursor()
        cur.execute("select * from weather")
        # обновление значения в базе данных
        cur.execute("update weather set date=:date, temperature=:temperature where idCity=:idCity",
                    {'date': date, 'temperature': temperature, 'idCity': idCity})

def listLocalID(baseName = baseName):
    '''
    функция обновляет значение температуры и меняет дату обновления в записи локальной базы по id города
    '''
    try:
        listID = []
        with sqlite3.connect(baseName) as conn:
            cur = conn.cursor()
            cur.execute("select * from weather")
            for row in cur.fetchall():
                idCity, city, country, date, temperature, idWeather = row
                listID.append(idCity)
        return listID
    except sqlite3.OperationalError:
        createBase()
        listLocalID()

parsCityListJson()      # освоили все исходные данные

viewValueBase('all')
