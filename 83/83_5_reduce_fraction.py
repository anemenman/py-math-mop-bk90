# -*- coding: utf-8 -*-
"""Сократить дробь. Даны натуральные числа m и n. Найти такие натуральные числа m1 и n1, не имеющие общих делителей,
что m1/n1 = m/n."""

# Алгоритм Евклида
m = 5000
n = 100000
is_reduce = False

for j in range(1, n + 1):
    print j
    i = j * m / n
    if i * n == j * m and m != i:
        print("RESULT: " + str(m) + "/" + str(n) + " = " + str(i) + "/" + str(j))
        is_reduce = True
        break

if not is_reduce:
    print("NO RESULTS")

print 10%6
