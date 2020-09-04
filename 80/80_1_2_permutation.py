# -*- coding: utf-8 -*-
"""Перестановки. Задан массив A[1:m] попарно различных чисел. Напечатать все перестановки этих чисел"""
import math

m = 4
p = range(1, m + 1)


def swap_elements(i, j, list):
    list[i] = list[i] + list[j]
    list[j] = list[i] - list[j]
    list[i] = list[i] - list[j]


def reverse_sublist(i, list):
    sub_list = list[i:]
    sub_list.reverse()
    list[i:] = sub_list


def find_max_j(i, list):
    j = len(list) - 1
    while j > i:
        if list[i] < list[j]:
            break
        j = j - 1
    return j


def next_process():
    result = False
    for i in range(m, 0, -1):
        if i != 1 and p[i - 2] < p[i - 1]:
            j = find_max_j(i - 2, p)
            swap_elements(i - 2, j, p)
            reverse_sublist(i - 1, p)
            result = True
            break
    return result


count = 1
while next_process():
    print(p)
    count = count + 1

print('Count of permutations: ' + str(count))
print('Factorial: ' + str(math.factorial(m)))
