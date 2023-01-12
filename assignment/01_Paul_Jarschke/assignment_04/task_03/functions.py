import math


def decimal2binary(n):
    # function to convert decimal integers to binary
    x = []
    while n > 0:
        x.append(n % 2)
        n = math.floor(n/2)
    return x[::-1]


def decimal_to_binary_correct(n):
    # function that converts decimal to binary correctly
    return int(bin(n).replace("0b", ""))
