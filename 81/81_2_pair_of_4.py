# -*- coding: utf-8 -*-
"""Пара четверок. Найти минимальное число, которое представляется суммой четырех квадратов натуральных чисел
не единственным образом."""
import sys
from math import sqrt

maxint = 1000
b = False
bi = False
n1 = 2  # Искомое число
i1 = j1 = k1 = p1 = 1  # 1-е представления числа n
i2 = j2 = k2 = p2 = 1  # 2-е представления числа n

print(sys.maxint)
for n in range(2, maxint):
    n1 = n
    b = False
    for i in range(1, int(sqrt(n))):
        i1 = i
        for j in range(1, i):
            j1 = j
            if i * i + j * j >= n:
                break
            for k in range(1, j):
                k1 = k
                if i * i + j * j + k * k < n:
                    p1 = int(sqrt(n - i * i - j * j - k * k))
                    if i * i + j * j + k * k + p1 * p1 == n and p1 <= k:
                        if b:
                            bi = True
                            break
                        i2 = i1
                        j2 = j1
                        k2 = k1
                        p2 = p1
                        b = True
            if bi:
                break
        if bi:
            break
    if bi:
        break

print("------------")
print("Results:")
print(str(n1) + "=" + str(i1) + "^2+" + str(j1) + "^2+" + str(k1) + "^2+" + str(p1) + "^2")
print(str(n1) + "=" + str(i2) + "^2+" + str(j2) + "^2+" + str(k2) + "^2+" + str(p2) + "^2")
