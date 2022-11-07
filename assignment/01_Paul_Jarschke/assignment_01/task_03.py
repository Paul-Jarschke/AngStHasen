# Task 03

# Write a program that reads in an upper bound (number) provided by the user and prints the sequence of Fibonacci numbers that are less or equal to the number given by the user.
# Use a while-loop for this task.

print('Please provide and upper bound for the Fibonacci sequence.')
upper_bound = int(input())

f_0 = 0
f_1 = 1
f_n = 0

print('Your Fibonacci Sequence is:')
print(str(f_0) + ', ' + str(f_1), end=', ')

while f_n < upper_bound:
    f_n = f_0 + f_1
    f_0 = f_1
    f_1 = f_n
    print(f_n, end=', ')

# funktioniert noch nicht :(
# gives 1 number too much
