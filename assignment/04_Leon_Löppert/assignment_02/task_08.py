################################################
#### Programing for Data Scientists: Python ####
####              Assignment 02             ####
####             by Leon Löppert            ####
################################################

# Task 08 – Unlimited Power ----

# Write a function with two arguments –  x  and  n . The function returns the value of  x^n . Use recursion.

def expo(x, n):
    xn = 0
    if n == 0:
        xn = 1
    elif n > 0:
        xn = x
        while n > 1:
            xn = xn * x
            n -= 1
    elif n < 0:
        n = n * (-1)
        xn = x
        while n > 1:
            xn = xn * x
            n -= 1
        xn = 1/xn
    print(f"The result is:\n{xn}")

x = input("For the equation x^n, give me a value of 'x':\n")
n = int(input("For the equation x^n, give me the power 'n' as an integer:\n"))

try:
    x = int(x)
except:
    x = float(x)

expo(x, n)
