# -*- coding: utf-8 -*-
"""Заданная сумма цифр. Составить программу вывода всех 3-х значных десятичных чисел, сумма цифр которых равна
 данному натуральному числу."""

n = 23
k = 0
c = 0
if n <= 27:
    for i in range(10):
        for j in range(10):
            c = c + 1
            k = n - i - j
            # print(k)
            if 9 >= k >= 1:
                print(i + 10 * j + 100 * k)

print("------")
print("Count: " + str(c))
