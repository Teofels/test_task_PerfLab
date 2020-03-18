import sys
import os
import pandas as pd


def append_column(data, file):
    '''
    Получает на вход датафрейм и файл с данными, считывает данные и добавляет в датафрейм как новую колонку
    :param data: датафрейм, с которым идет работа
    :param file: файл, откуда считывать данные
    :return: датафрейм с новой колонкой
    '''
    with open(directory + '/' + file) as f:
        temp = f.read().splitlines()  # сюда считываюся данные из файла
    temp = [float(item) for item in temp]  # тут преобразуются в тип float, так как были str
    df[file] = temp  # создает колонку с названием файла и содержанием - содержание файла


directory = sys.argv[1]  # получение пути к каталогу с файлами
files = os.listdir(directory)  # получения списка файлов в полученной дериктории

df = pd.DataFrame()  # инициализация датафрейма для данных из файла, чтобы удобнее визуализировать
for i in files:
    append_column(df, i)  # наполнение датафрейма данными из файлов с помощью вспомогательной функции

df['sum'] = df['Cash1.txt'] + df['Cash2.txt'] + df['Cash3.txt'] + df['Cash4.txt'] + df['Cash5.txt']
# создание новой колонки, в которой содержится сумма средней длины очереди в кассу для каждого интервала

index_of_max = df['sum'].idxmax()  # поиск индекса с максимальным значением

interval = index_of_max + 1  # так как интервалы считаются с 1

print(interval)  # вывод в консоль результата
