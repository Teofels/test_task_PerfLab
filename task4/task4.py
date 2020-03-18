import sys


file_name = sys.argv[1]  # получение файла с временем посещения

with open(file_name) as f:
    time_data = f.read().splitlines()

time_in_minutes = []
# преобразование исходных данных в вид: (время входа, время выхода) , причем время в минутах
for i in time_data:
    a, b = i.split(' ')
    a1, a2 = map(int, a.split(':'))
    b1, b2 = map(int, b.split(':'))
    time_in_minutes.append((a1*60 + a2, b1*60 + b2))

visitors_per_minute = {}
# расчет сколько было посетителей в каждую минуту работы банка
# данные хранятся в словарь, где ключ - время, а значение - кол-во посетителей в это время
for i in range(8*60, 20*60 + 1):
    temp = 0
    for enter, exit in time_in_minutes:
        if enter <= i < exit:
            temp += 1
    visitors_per_minute[i] = temp

# определение сколько максимально было посетителей и когда это в первый раз произошло
max_key = max(visitors_per_minute, key=visitors_per_minute.get)
max_value = visitors_per_minute[max_key]

periods_of_max_visitors = []  # лист, в которм будут хранится период(-ы) с макс кол-вом посетителей
begin = max_key  # точка отсчета, момент когда макс кол-во посетителей впервые встрелось
period = 1  # период, сколько минут макс кол-во "просуществовало"

for i in range(max_key, 20*60):  # проходим по времени работы банка, до предпоследней минуты
    if (visitors_per_minute[i] != max_value) and (visitors_per_minute[i+1] != max_value):
        # если текущая минута и следующая не содержат макс кол-во клиентов, то ничего не делаем
        continue
    elif(visitors_per_minute[i] != max_value) and (visitors_per_minute[i+1] == max_value):
        # если текущая минута не содержит макс кол-ва клиентов, а следующая содержит,
        # то перезаписываем значение начала периода, когда было макс кол-во клиентов
        begin = i + 1
    else:
        # если текущая минута содержит макс кол-во клиентов
        if visitors_per_minute[i+1] == max_value:
            # и следующая минута тоже, то увеличиваем период на 1
            period += 1
        else:
            # а следующая уже нет, то записываем период когда было макс кол-во клиентов в лист
            periods_of_max_visitors.append((begin, begin+period))
            period = 1

for begin, end in periods_of_max_visitors:
    # красиво выводим полученный результат
    print('{:d}:{:02d} {:d}:{:02d}'.format(begin//60,begin%60, end//60, end%60))
