# -*- coding: utf-8 -*-
"""Напечатать все простые. не превосходящие M"""
import time

"""Решето Эратосфена"""


def is_prime(sieve_of_eratosthenes, number):
    result = True
    for prime in sieve_of_eratosthenes:
        if number % prime == 0:
            result = False
            break
    return result


ts_start = time.time()
m = 1000000
number = 3
prime_numbers = [2]
sieve_of_eratosthenes = [2]

for i in range(3, m, 2):
    # print(i)
    if is_prime(sieve_of_eratosthenes, i):
        prime_numbers.append(i)
        if i ** 2 <= m:
            sieve_of_eratosthenes.append(i)

ts_end = time.time()

print('=======')
print(prime_numbers)
print(sieve_of_eratosthenes)
print(m ** 0.5 / 2)
print(str(len(sieve_of_eratosthenes)) + ' < ' + str(m ** 0.5 / 2))
print('Time in seconds: ' + str(ts_end - ts_start))  # 0.9
