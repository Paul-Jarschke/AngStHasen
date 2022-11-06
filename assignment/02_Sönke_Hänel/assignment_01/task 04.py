### Task 04 –Selective Printing
# Write a program that reads in an upper bound (number) provided by the user and prints all integer numbers that are
# less or equal to the upper bound except the integer numbers that are divisible by 3.
# Use the continue statement. For example, if the user enters 6 as the upper bound, the output should be 0, 1, 2, 4, 5.

# input reception
input_bound = int(input("Provide an upper bound (number) please.\n"))

# loop for printing every integer that isn't a multiple of 3 up until the input_bound
i = -1
while (i < input_bound):
    i += 1
    if (i % 3 == 0):
        continue
    print(i)
