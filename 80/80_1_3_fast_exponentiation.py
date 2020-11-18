# -*- coding: utf-8 -*-
"""Быстрая степень. Ввести вещественное число A и натуральное k. Вычислить и напечатать A**k с выполнением следующих
условий: операцией возведения в степень пользоваться нельзя; k может оказаться настолько большим, что недопустимо
выполнять k умножений"""

a = aa = 20
k = kk = 100000

b = 1

count = 0

while k > 0:
    count = count + 1
    if k % 2 == 0:
        k = k / 2
        a = a * a
    else:
        k = k - 1
        b = b * a
    print('k = ' + str(k))
    print('b = ' + str(b))
    print('------')

print('Result: ' + str(b))
print('Count: ' + str(count))  # 15!!!
print('A**k: ' + str(aa ** kk))
