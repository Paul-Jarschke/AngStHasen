import math


def decimal2binary(n):
    # function to convert decimal integers to binary
    x = []
    while n > 0:
        x.append(n % 2)
        n = math.floor(n / 2)
    return x[::-1]


def decimal2binary_correct(n):
    # function to convert decimal integers to binary
    x = ''
    if n == 0:
        return f'0'
    if n < 0:
        n = -n
        flag = f'-'
    else:
        flag = f''
    while n > 0:
        x = f'{n % 2}{x}'
#        x.append(n % 2)
        n = math.floor(n / 2)

    return f'{flag}{x}'

