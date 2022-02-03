# -*- coding: utf-8 -*-
"""Многочлен.

Вычислить коэф a[0], a[1], ... a[n-1] многочлена
P(x) = a[0] + a[1]*x + a[2]*x^2 + ...
с заданными действительными корнями x[1],x[2],...

Напоминание: по теореме Безу
P(x) = (x-x[1])*(x-x[2])*...."""

from numpy.polynomial.polynomial import polyfromroots

print 'Numpy:'
print polyfromroots((1, 2, 3))
print polyfromroots((2, 1, 3))
print '------------------------------------------------'

# x = [1, 2, 3]
# a = [0, 0, 0]
# print x
#
# a[0] = -x[1]
# a[1] = 1
# print a
#
# m = 2
# N = len(x)
# print N
#
# while m < N:
#     a[m - 1] = a[m - 2] - x[m]
#     i = m - 2
#     while i >= 1:
#         a[i] = a[i - 1] - a[i] * x[m]
#         i = i - 1
#     a[0] = -a[0] * x[m]
#     m = m + 1
#
# print '------------------------------------------------'
# print a
print 'Fin'
