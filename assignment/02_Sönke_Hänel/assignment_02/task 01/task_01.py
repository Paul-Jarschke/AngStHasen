# Task 01 – String Length
#
# Write a program that reads in a string and prints the length of the input string.
# Do not use any built-in functions of Python, such as len().
# For example, if the input is “Computer Science”, the output should be length: 16.

name = input("Please enter a string!\n")
i = 0
for x in name:
    i += 1
print(i)
