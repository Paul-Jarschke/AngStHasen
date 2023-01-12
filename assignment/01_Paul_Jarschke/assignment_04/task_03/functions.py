# This file provides two different functions that transform decimal to binary
import math


def decimal2binary(n):
    # function that converts decimal to binary (false transformation)
    x = []
    while n > 0:
        x.append(n % 2)
        n = math.floor(n/2)
    return x[::-1]


def decimal_to_binary_correct(n):
    # function that converts decimal to binary (correct transformation)
    return int(bin(n).replace("0b", ""))
