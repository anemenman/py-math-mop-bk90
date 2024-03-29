# -*- coding: utf-8 -*-
"""Сумма кубов.

Сколькими способами заданное натуральное число N можно представить в виде суммы двух кубов натуральных чисел:
N = i^3 + j^3?

Перестановка слагаемых нового способа не дает. Операцией возведения в степень 1/3 ползоваться нельзя."""

N = 35
m = 0
i = 1

j = round((N - 1) ** (1.0 / 3.0))

print j

while i <= j:
    print str(i) + ' and ' + str(j)
    while True:
        k = i * i * i + j * j * j
        print k
        if k == N:
            m = m + 1
            print str(i) + '^3 + ' + str(j) + '^3 = ' + str(N) + ' ---> ' + str(m)
        if k <= N:
            i = i + 1
        if k >= N:
            j = j - 1

        if i > j:
            break

print 'Fin'
