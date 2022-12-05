################################################
#### Programing for Data Scientists: Python ####
####              Assignment 02             ####
####             by Leon Löppert            ####
################################################

# Task 03 – Character Frequency ----

# Write a program that:

# Reads in a string and removes any spaces from the string
# Counts how often individual characters occur in the string
# Stores the information on character occurrence frequency in a dictionary
# Prints the dictionary.
# For example, if the input is “santa claus”, the output should be:
# {'s': 2, 'a': 3, 'n': 1, 't': 1, 'c': 1, 'l': 1, 'u': 1}.

input = str(input("Please provide me an input:\n"))
input = input.replace(" ", "")
cdict = dict()

inpset = set(input)
for letter in inpset:
    count = input.count(letter)
    cdict[letter] = count

print("\n" + "This is your dictionary:\n" + str(cdict))
    # Does differentiate between upper-  and lower case.

