# -*- coding: utf-8 -*-
"""Сумма квадратов. Можно ли заданное натуральное число M представить в виде суммы двух квадратов натуральгых чисел?"""

m = 1000000

i = 1
j = 2
result = False
k = 1
while 2 * i * i <= m:
    j = int((m - i * i) ** 0.5)
    if i * i + j * j == m:
        result = True
        break
    i = i + 1
    k = k + 1

print(k)
if result:
    print(str(i) + "^2 + " + str(j) + "^2 = " + str(m))
else:
    print("No solution")
