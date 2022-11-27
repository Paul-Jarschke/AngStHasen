################################################
#### Programing for Data Scientists: Python ####
####              Assignment 01             ####
####             by Leon Löppert            ####
################################################

# Task 02 – Reversed Words ----

# Write a program that reads in a word provided by the user and prints the word in a reversed order. For example,
# if the input is hello, the output should be ‘olleh’.

    # a) Using just array indices
stringreverse = input("Give me a string to reverse: \n")[::-1]
print(f"The reversed string is: {stringreverse}")

    # b) Using a loop structure
string = input("Give me a string to reverse: \n")
stringreverse2 = ""
for index, letter in enumerate(string):
    stringreverse2 = string[index] + stringreverse2
print(stringreverse2)
