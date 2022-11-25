# Task 01 - String Length
# Write a program that reads in a string and prints the length of the input string. Do not use any built-in functions of
# Python, such as len(). For example, if the input is “Computer Science”, the output should be length: 16.

word = str(input('Please enter a string:\n'))

length = 0
for i in word:
    length += 1

print(f'Length of your string: {length}')
