# -*- coding: utf-8 -*-
"""Слияние массивов. Даны два числа m и n и два упорядоченных массива A[1]<=A[2]<=...<=A[m] и B[1]<=B[2]<=...<=B[n].
Образовать из этих элементов упорядоченный массив C[1]<=C[2]<=...<=C[m+n]."""

a = [1, 3, 5, 7, 9]
b = [1, 2, 3, 4, 4, 4, 4, 5]

m = len(a)
n = len(b)

c = x = [0 for i in range(m + n)]

print(len(c))
print(c)

k = i = j = 0

while k < m + n:
    if i >= m:
        c[k] = b[j]
        j = j + 1
    elif j >= n:
        c[k] = a[i]
        i = i + 1
    elif a[i] > b[j]:
        c[k] = b[j]
        j = j + 1
    else:
        c[k] = a[i]
        i = i + 1
    k = k + 1

print("RES:")
print c
