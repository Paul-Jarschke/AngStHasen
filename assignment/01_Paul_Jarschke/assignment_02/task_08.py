# Task 08 - Unlimited Power
# Write a function with two arguments – x and n. The function returns the value of xn. Use recursion.

# user input
x = int(input('Which number do you want to multiply with itself ?\n'))
n = int(input('How often do you want to multiply the number with itself ?\n'))


def power(base, exponent):
    """Recursive function that multiplies x n-times with itself."""
    # base case
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base

    # recursive case
    else:
        return base * power(base, (exponent - 1))


# output
print(f'Your result is: {power(base=x, exponent=n)}')
