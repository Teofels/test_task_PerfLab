import numpy as np
import sys


file_name = sys.argv[1] # получение имени файла из аргументов коммандной строки

with open(file_name) as f:
    data = f.read().splitlines() # считывание данных из файла

data = [int(item) for item in data] # преобразование данных в тип int, так как считаались они как str
data = np.array(data)

data_percentile = round(np.percentile(data, 90), 2) # расчет 90 перцентиль и  округление до 2-х знаков после запятой
data_median = round(np.median(data), 2) # расчет медианы
data_max = round(max(data), 2) # поиск максимального значения
data_min = round(min(data), 2) # поиск минимального значения
data_mean = round(np.mean(data), 2) # расчет среднего значения

# вывод полученных данных:
print(data_percentile)
print(data_median)
print(data_max)
print(data_min)
print(data_mean)
