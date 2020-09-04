# -*- coding: utf-8 -*-
"""Различные числа. Задан массив A[1:m]. Сосчитать и напечатать, сколько различных чисел в этом массиве и каких"""

a = [1, 1, 4, 5, 6, 4, 8, 9, 7, 11, 12, 13, 14, 15, 11, 3, 20, 100, 67, 101, 100]  # 1,4,11,100

b = []
k = 0
for i in range(len(a)):
    if a[i] in b:
        continue
    for j in range(i + 1, len(a)):
        k = k + 1
        if a[i] == a[j]:
            b.append(a[i])
            break

print("i^2 = " + str(len(a) ** 2) + ", k = " + str(k) + ", min = " + str(len(a) * len(b)))
print(b)
