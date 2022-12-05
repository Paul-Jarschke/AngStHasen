################################################
#### Programing for Data Scientists: Python ####
####              Assignment 02             ####
####             by Leon Löppert            ####
################################################
import math

# Task 09 – Unlimited Power ----

# Using function for factorial and function x^n from previous task, write a program that reads value of x and
# prints approximate value of e^x. Use this formula (Taylor series) for calculation:
# e^x=1+x+(x^2)/(2!)+(x^3)/(3!)+...+(x^n)/(n!)

# To get precise value of  e^x , the series would have to be infinite. Suppose that there is some required accuracy,
# so the calculation finishes as soon as the value of the next element is smaller than given threshold (e.g., 0.000001).

import math

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

x = int(input("For the equation e^x give me a value for 'x':\n"))

sol = [0]
n = 0

while True:
    sol.append(sol[n] + x**n/math.factorial(n))
    if sol[n + 1] - sol[n]  <  0.000001:
        break
    n = n + 1

print(f"The taylor-approximation for e^{x} is:\n{sol[n + 1]}")






