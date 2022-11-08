# Task 03

# Write a program that reads in an upper bound (number) provided by the user and prints the sequence of Fibonacci numbers that are less or equal to the number given by the user.
# Use a while-loop for this task.

print('Please provide and upper bound for the Fibonacci sequence.')
upper_bound = int(input())

f_0 = 0  # First Number of Fibonacci Sequence
f_1 = 1  # Second Number of Fibonacci Sequence
f_n = 1  # Iteration Variable

if upper_bound == 0:
    print(f'Your Fibonacci Sequence is:\n{f_0}')

elif upper_bound == 1:
    print(f'Your Fibonacci Sequence is:\n{f_0}, {f_1}, {f_1}')

else:
    print('Your Fibonacci Sequence is:')
    print(f_0, end='')

    while f_n <= upper_bound:
        f_n = f_1 + f_0
        f_0 = f_1
        f_1 = f_n
        print(f', {f_0}', end='')
