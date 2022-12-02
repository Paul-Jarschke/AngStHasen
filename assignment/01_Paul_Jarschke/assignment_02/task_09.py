# Task 09 - Unlimited Power II
# Using function for factorial and function xn from previous task, write a program that reads value of x and prints
# approximate value of ex. Use this formula (Taylor series) for calculation.
# To get precise value of ex, the series would have to be infinite. Suppose that there is some required accuracy, so the
# calculation finishes as soon as the value of the next element is smaller than given threshold (e.g., 0.000001).


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


def factorial(n):
    """Recursive function that returns the factorial of n."""
    # base case
    if n == 0:
        return 1
    elif n == 1:
        return 1

    # recursive case
    else:
        return n * factorial(n-1)


# ask user for input
x = int(input('Please enter an exponent for e^x:\n'))

# initiate global vars for loop
i = 0
added_term = 1
taylor_approx = 0

# loop that sums up all parts of the taylor series until the threshold is met
while added_term > 0.000001:
    # compute term of the sum for i
    added_term = power(base=x, exponent=i) / factorial(i)
    # sum additive terms to compute taylor approximation
    taylor_approx += added_term
    i += 1

print(f'The Taylor Series approximation for e^{x} = {taylor_approx}')
