# -*- coding: utf-8 -*-
"""Системы счисления. В массиве М[1:9] записаны разряды (цифры) некоторого натурального числа в i-ричной системе
счисления (М[1] - разряд едениц и т.д.). Отпечатать разряды этого числа в j-ричной системе счисления, начиная с разряда
единиц. Числа i, j не превосходят 10."""

# Схема Горнера
# n = ((...(m[9]*i + m[8])*i + ... + m[2])*i + m[1]
m = [9, 8, 7, 6, 5, 4, 3, 2, 1]
i = 10
j = 8
n = 0

for k in range(8, -1, -1):
    # print m[k]
    n = n * i + m[k]

print n

print "(Слева разряд единиц) в " + str(j) + "-ричной системе"
while True:
    print n % j
    n = n / j
    if n <= 0:
        break

# print 5 % 3
# print 7 / 3
