import sys


def place_of_point(quad, point):
    '''
    Определяет положение точки относительно выпуклого четырехугольника.
    Возвращает:
    0 - точка на одной из вершин
    1 - точка на одной из сторон
    2 - точка внутри
    3 - точка снаружи

    quad: координаты вершин выпуклого четырехугольника
    point: координаты точки, положение которой проверяется
    '''
    point_x = point[0]  # координата x проверяемой точки
    point_y = point[1]  # координата y проверяемой точки

    if point in quad:
        return 0  # если координата точки совпадает с координатами вершины четырехугольника
    if point_on_line(quad, point_x, point_y) == 1:
        return 1
    if inPolygon(quad, point_x, point_y) == 1:
        return 2
    return 3  # в случае, если точка не находится не в вершинах, не на сторонах и не внутри четырехугольника
    # значит она находится вне четырехугольника


def point_on_line(quad, point_x, point_y):
    '''
    Проверяет лежит ли искомая точка на одной из сторон выпуклого четырехугольника
    :param quad: координаты вершин выпуклого четырехугольника
    :param point_x: координата x проверяемой точки
    :param point_y: координата y проверяемой точки
    :return: 1 - если точка лежит на одной из сторон четырехугольника, -1 - если не лежит
    '''
    for i in range(len(quad)):
        cor_x1 = quad[i][0]
        cor_y1 = quad[i][1]
        cor_x2 = quad[i - 1][0]
        cor_y2 = quad[i - 1][1]

        # с помощью уравнения проверяется принадлежность точки к прямой, образуемой двумя соседними точками четырехугольника
        # далее проверяется, что точка лежит в пределах стороны четырехугольника
        if ((cor_y1 - cor_y2) * point_x + (cor_x2 - cor_x1) * point_y + (cor_x1 * cor_y2 - cor_x2 * cor_y1)) == 0 \
                and ((point_x >= cor_x1 and point_x <= cor_x2) or (point_x <= cor_x1 and point_x >= cor_x2)) \
                and ((point_y >= cor_y1 and point_y <= cor_y2) or (point_y <= cor_y1 and point_y >= cor_y2)):
            return 1
    return -1


def inPolygon(quad, point_x, point_y):
    '''
    Проверяет находится ли точка внутри четырехугольника
    :param quad: координаты вершин выпуклого четырехугольника
    :param point_x: координата x проверяемой точки
    :param point_y: координата y проверяемой точки
    :return: возвращает переменную c, если c = 1, то точка лежит в пределах четырехугольника
    '''
    xp = []
    yp = []
    # преобразование пар координат вершин в два массива
    for i in quad:
        xp.append(i[0])
        yp.append(i[1])

    c = 0
    for i in range(len(xp)):
        if (((yp[i] <= point_y and point_y < yp[i - 1]) or (yp[i - 1] <= point_y and point_y < yp[i])) and \
                (point_x > (xp[i - 1] - xp[i]) * (point_y - yp[i]) / (yp[i - 1] - yp[i]) + xp[i])):
            c = 1 - c
    return c


file_1 = sys.argv[1]  # получение файла с координатами вершин четырехугольника
file_2 = sys.argv[2]  # получение файла с координатами проверяемых точек

data_quad = []
#  считывание данных о вершинах четырехугольника
with open(file_1) as f:
    for line in f:
        a, b = map(float, line.split())
        data_quad.append((a, b))

data_points = []
#  считывание данных о точках
with open(file_2) as f:
    for line in f:
        a, b = map(float, line.split())
        data_points.append((a, b))

for point in data_points:
    print(place_of_point(data_quad, point))  # для каждой точки проверяется ее местоположение и выводится в консоль
