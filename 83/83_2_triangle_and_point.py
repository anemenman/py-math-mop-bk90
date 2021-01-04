# -*- coding: utf-8 -*-
"""Треугольник и точка. Заданы прямоугольные координаты x1, y1; x2, y2; x3, y3 вершин треугольника и координаты
x, y точки. Определить и напечатать, находится ли точка в треугольнике. Погрешностями вычислений пренебречь."""
from math import sqrt


def s(x1, y1, x2, y2, x3, y3):
    xy12 = sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
    xy13 = sqrt(pow((x1 - x3), 2) + pow((y1 - y3), 2))
    xy23 = sqrt(pow((x2 - x3), 2) + pow((y2 - y3), 2))

    p = 0.5 * (xy12 + xy13 + xy23)

    # Формула Герона
    s = sqrt(p * (p - xy12) * (p - xy13) * (p - xy23))

    return s


a1 = 1
b1 = 2

a2 = 5
b2 = 1

a3 = 7
b3 = 3

ax = 4
bx = 2

delta = 1.00001

s123 = s(a1, b1, a2, b2, a3, b3)
print("s123 = " + str(s123))

s12x = s(a1, b1, a2, b2, ax, bx)
print("s12x = " + str(s12x))

s13x = s(a1, b1, ax, bx, a3, b3)
print("s13x = " + str(s13x))

s23x = s(ax, bx, a2, b2, a3, b3)
print("s23x = " + str(s23x))

s123x = s12x + s13x + s23x
print("s123x = " + str(s123x))

if s123x > delta * s123:
    print ("NO")
else:
    print("YES")
