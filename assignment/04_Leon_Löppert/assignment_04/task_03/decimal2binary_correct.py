import math

def decimal_to_binary_correct(n):
    # function to convert decimal integers to binary
    x = []
    sign = 1
    if n < 0:
        sign = -1
        n *= -1
    elif n == 0:
        x.append(0)
    while n > 0:
        x.append(n % 2)
        n = math.floor(n/2)
    binary = x[::-1]
    return int(''.join([str(d) for d in binary]))*sign

