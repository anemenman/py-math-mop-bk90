# -*- coding: utf-8 -*-
"""Числа из разных цифр. Напечатать все 4-х значные натуральные числа, в десятичной записи которых нет
2-х одинаковых цифр."""

count = 0

for i in range(0, 10):
    for j in range(0, 10):
        if i != j:
            for k in range(0, 10):
                if k != i and k != j:
                    for m in range(0, 10):
                        if m != i and m != j and m != k:
                            count = count + 1
                            print i * 1000 + j * 100 + k * 10 + m

print "--------"
print count
