################################################
#### Programing for Data Scientists: Python ####
####              Assignment 02             ####
####             by Leon Löppert            ####
################################################
import random

# Task 02 – Largest List Element ----

# Write a program that generates a list of 10 random integers between 1 and 100 and then finds and prints the
# largest element in the list. Do not use the built-in function max(). For example, if the input is
# [23,3,42,29,12,15,8,4,37,34], the output should be the largest element: 42.

import random
random_ints = []
i = 0


while i <= 9:
    random_ints.append(random.randrange(1, 100))
    i += 1
print("My list of random integers is:\n" + str(random_ints) + "\n")

maximum = 0
for index, int in enumerate(random_ints):
    if random_ints[index] > maximum:
        maximum = random_ints[index]

print("The largest number of this list is:\n" + str(maximum))

