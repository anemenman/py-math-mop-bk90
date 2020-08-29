# -*- coding: utf-8 -*-
"""Арифметические действия. В написанном выражении ((((1?2)?3)?4)?5)?6 вместо каждого знака ? вставить знак одного из
четырех арифметических действий: + - * / так, чтобы результат вычислений равнялся 35 (при делении дробная часть
в частном отбрасывается). Достаточно найти одно решение."""


def calc(a, b, op):
    # +
    if op == 1:
        return a + b
    # -
    elif op == 2:
        return a - b
    # //
    elif op == 3:
        return a // b
    # *
    else:
        return a * b


# operators = [1, 2, 3, 4]
m = 35
b = range(6)
b[0] = 1
# init b with op is +
for i in range(1, 6):
    # print(i)
    b[i] = calc(b[i - 1], i + 1, 1)
#
# print(b)
# # init w
# w = b[5]
# print(w)

a = [4, 4, 4, 4, 4]
k = 0
max_k = 4 ** 5
while True:
    for i in range(5, 0, -1):
        # print(i)
        if a[i - 1] == 4:
            a[i - 1] = 1
        else:
            a[i - 1] = a[i - 1] + 1
            b[i] = calc(b[i - 1], i + 1, a[i - 1])

            for j in range(i + 1, 6):
                b[j] = calc(b[j - 1], j + 1, a[j - 1])

            k = k + 1
            print(a)
            if b[5] != m:
                break
    if b[5] == m or k >= max_k:
        break
print('Решение найдено: ' + str(b[5] == m))
print('Max k = ' + str(max_k))
print('k = ' + str(k))
print(b)
print(a)

print(((((1 + 2) + 3) * 4) + 5) + 6)
