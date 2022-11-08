# Task 4

# Write a program that reads in an upper bound (number) provided by the user and prints all integer numbers that are
# less or equal to the upper bound except the integer numbers that are divisible by 3.
# Use the continue statement. For example, if the user enters 6 as the upper bound, the output should be 0, 1, 2, 4, 5.

# Hint for Tutor:
# 0 is divisible by 3 and should not be p. In the given example 0 is printed out which is why I print 0 as well.

print('Please provide and upper bound (number) for sequence.')
upper_bound = int(input())

print(0, end='')

i = -1
while i <= upper_bound - 1:
    i += 1
    if i % 3 != 0:
        print(f', {i}', end='')
    continue
