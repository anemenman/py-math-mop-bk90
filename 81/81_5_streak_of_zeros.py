# -*- coding: utf-8 -*-
"""Серия нулей. Задан числовой массив A[1:n]. Найти длину самой длинной последовательности подряд идущих элементов
массива, равных нулю."""

n = 10
res = [0 for i in range(n)]
res[1] = 1
res[7] = 1
print res
t = 0
max = 0

for i in range(0, n):
    if res[i] != 0:
        if max < t:
            max = t
            t = 0
    else:
        t = t + 1

if max < t:
    max = t

print "--------"
print max
