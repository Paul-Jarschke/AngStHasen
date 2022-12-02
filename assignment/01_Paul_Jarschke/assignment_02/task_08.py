# Task 08 - Unlimited Power
# Write a function with two arguments – x and n. The function returns the value of xn. Use recursion.

# user input
base = int(input('Which number do you want to multiply with itself ?\n'))
exponent = int(input('How often do you want to multiply the number with itself ?\n'))


def power(x, n):
    """Recursive function that multiplies x n-times with itself"""
    # base case
    if n == 0:
        return 1
    elif n == 1:
        return x

    # recursive case
    else:
        return x * power(x, (n-1))


# output
print(f'Your result is {power(base, exponent)}')
