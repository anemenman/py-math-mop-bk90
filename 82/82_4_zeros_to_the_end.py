# -*- coding: utf-8 -*-
"""Нули в конец. Дан одномерный массив. Все его элементы не равные нулю, переписать (сохраняя их порядок) в начало
массива, а нулевые элементы - в конец массива(новый массивне заводить)."""

n = 10
x = [0 for i in range(n)]
x[0] = 1
x[6] = 10
x[7] = 3

print x

j = -1
for i in range(n):
    if x[i] != 0:
        j = j + 1
        if j < i:
            x[j] = x[i]
            x[i] = 0

print x