# -*- coding: utf-8 -*-
"""M+1 в двоичной записи. Целое неотрицательное число M задано массивом двоичных цифр a0, a1, ..., an-1.
Напечатать массив двоичных цифр числа M+1."""

a = [1, 0, 0, 1, 0, 1, 1, 1]  # 151


def print_list_to_dec_str(a):
    a_str = ''
    for i in range(len(a)):
        a_str = a_str + str(a[i])

    print(a_str)
    print(int(a_str, 2))


def m_plus_1(a):
    increase_list = True
    for i in range(len(a) - 1, -1, -1):
        if a[i] == 1:
            a[i] = 0
        else:
            a[i] = 1
            increase_list = False
            break

    if increase_list:
        a.insert(0, 1)


print_list_to_dec_str(a)

print("------")
m_plus_1(a)
print_list_to_dec_str(a)

print("-------")
b = [1, 1, 1]  # 7
print_list_to_dec_str(b)

print("-------")
m_plus_1(b)  # 8
print_list_to_dec_str(b)
