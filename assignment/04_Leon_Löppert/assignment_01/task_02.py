################################################
#### Programing for Data Scientists: Python ####
####              Assignment 01             ####
####             by Leon Löppert            ####
################################################

# Task 02 – Reversed Words ----

# Write a program that reads in a word provided by the user and prints the word in a reversed order. For example,
# if the input is hello, the output should be ‘olleh’.

stringreverse = input("Give me a string to reverse: \n")[::-1]
print(f"The reversed string is: {stringreverse}")
