"""Task 03 – Unity Test

The following algorithm in Python converts numbers in decimal representation to binary.

    Develop a unit test that checks for values in the interval [-1,3] whether the algorithm returns the expected results.
    Adjust the algorithm, so it passes the unit test developed in 1). Rename the function to

decimal_to_binary_correct()
"""
import math


def decimal2binary(n):
    # function to convert decimal integers to binary
    x = []
    while n > 0:
        x.append(n % 2)
        n = math.floor(n / 2)
    return x[::-1]


print(decimal2binary(5))
