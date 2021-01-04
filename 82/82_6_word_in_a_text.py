# -*- coding: utf-8 -*-
"""Вхождение слова в текст. Даны два целочисленных массива X[1:n] и Y[1:k]. Можно ли в первом из них выбрать такие k
идущих подряд элементов X[i+1], X[i+2],..., X[i+k] чтобы X[i+1]=Y[1], X[i+2]=Y[2],..., X[i+k]=Y[k]? Написать программу,
которая решает эту задачу и печатает ответ ДА или НЕТ."""

x = [0, 0, 1, 2, 3, 4, 5, 0, 0, 0]
n = len(x)
y = [1, 2, 3, 4, 5]
k = len(y)

print n
print k

res = False
for i in range(n - k):
    for j in range(k):
        if x[i + j] != y[j]:
            break
        else:
            print("YES from element: " + str(i))
            res = True
            break
    if res:
        break
