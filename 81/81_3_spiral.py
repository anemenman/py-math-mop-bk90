# -*- coding: utf-8 -*-
"""Спираль. Ввести число n и заполнить двумерный массив размером n x n числами 1, 2, ... по спирали(рис 1.1)."""

n = 9
res = [[0] * n for i in range(n)]
print(n)
k = i = j = 0
done = False


def ak():
    global k, done
    k = k + 1
    res[i][j] = k
    if k == n * n:
        done = True


while True:
    if done:
        break
    ak()
    j = j + 1
    while i + j < n - 1:
        ak()
        if done:
            break
        j = j + 1

    if done:
        break
    ak()
    i = i + 1
    while i < j:
        ak()
        if done:
            break
        i = i + 1

    if done:
        break
    ak()
    j = j - 1
    while i + j > n - 1:
        ak()
        if done:
            break
        j = j - 1

    if done:
        break
    ak()
    i = i - 1
    while i > j + 1:
        ak()
        if done:
            break
        i = i - 1
    if done:
        break

print(res)
print("----------")
for row in res:
    print(row)
