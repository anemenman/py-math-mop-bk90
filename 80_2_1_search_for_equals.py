# -*- coding: utf-8 -*-
"""Поиск рвных. Дан массив A[1:2, 1:15]. Известно, что среди его элементов два и только два равны между собой.
Напечатать их индексы."""

n = 2
m = 15
k = 1
a = [[0] * n for i in range(m)]

k = 1
# init
for j in range(m):
    for i in range(n):
        a[j][i] = k
        k = k + 1
a[14][0] = 2
print a  # a[0][1] == a[14][0]

print("------")
result = False
for i in range(m):
    for j in range(n):
        for p in range(m):
            if i < p:
                b = 0
            else:
                b = j + 1
            for q in range(b, n):
                if a[i][j] == a[p][q]:
                    print("a[" + str(i) + "][" + str(j) + "]==a[" + str(p) + "][" + str(q) + "]")
                    result = True
                    break
            if result:
                break
        if result:
            break
    if result:
        break
