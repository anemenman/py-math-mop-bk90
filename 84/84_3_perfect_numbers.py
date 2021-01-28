# -*- coding: utf-8 -*-
"""Совершенные числа. Натуральное число называется совершенным, если оно равно сумме всех своих собственных делителей,
вклюсая 1. Напечатать все совершенные числа, меньше, чем заданное M."""

m = 10000
k = 0

for i in range(2, m + 1):

    s = j = 1

    # do-while
    j = j + 1
    k = i / j
    if i == k * j and j <= k:
        s = s + j
        if j < k:
            s = s + k

    while j < k:
        j = j + 1
        k = i / j
        if i == k * j and j <= k:
            s = s + j
            if j < k:
                s = s + k
    if s == i:
        print("RESULT: " + str(i))

print("END")
