# Task 09 – Unlimited Power II
#
# Using function for factorial and function x^n from previous task,
# write a program that reads value of x and prints approximate value of e^x.
# Use this formula (Taylor series) for calculation
#
# e^x = 1 + x + x²/2! + x³/3! + ... + x^n/n!
#
# To get precise value of e^x, the series would have to be infinite.
# Suppose that there is some required accuracy,
# so the calculation finishes as soon as the value of
# the next element is smaller than given threshold (e.g., 0.000001).
import math

def tower_of_power(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        return x * tower_of_power(x, n - 1)

def euler_of_power(x, threshold=0.000001):
    eule_sum = 0
    i = 0
    while (tower_of_power(x, i)) / math.factorial(i) >= threshold:
        eule_sum += (tower_of_power(x, i)) / math.factorial(i)
        i += 1
    return eule_sum

# todo (maybe) also integrate the potency of negative integers?
