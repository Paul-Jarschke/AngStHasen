# Task 08 – Unlimited Power
#
# Write a function with two arguments – x and n. The function returns the value of x^n. Use recursion.

def tower_of_power(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        return x * tower_of_power(x, n - 1)

# # Test
# print(tower_of_power(3, 4))
