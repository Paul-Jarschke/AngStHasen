################################################
#### Programing for Data Scientists: Python ####
####              Assignment 02             ####
####             by Leon Löppert            ####
################################################

# Task 01 - String Length ----

# Write a program that reads in a string and prints the length of the input string. Do not use any built-in functions
# of Python, such as len(). For example, if the input is “Computer Science”, the output should be length: 16.

word = input("Type something and I count the length of it:\n")
i = 0

for letter in word:
    i = i + 1

print("The length of your string is " + str(i) + ".")
