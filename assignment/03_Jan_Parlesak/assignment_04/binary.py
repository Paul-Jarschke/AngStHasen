import unittest
import math

def decimal2binary(n):
    # function to convert decimal integers to binary
    x = []
    while n > 0:
        x.append(n % 2)
        n = math.floor(n/2)
    return x[::-1]


def decimal2binary_correct(n):
    # function to convert decimal integers to binary
    x = []
    if n<0:
        x.append(-1)
    if n==0:
        x.append(0)
    while n > 0:
        x.append(n % 2)
        n = n // 2
    return int(''.join(map(str,x[::-1])))


