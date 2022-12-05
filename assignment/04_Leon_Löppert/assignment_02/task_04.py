################################################
#### Programing for Data Scientists: Python ####
####              Assignment 02             ####
####             by Leon Löppert            ####
################################################

# Task 04 – Sorted List of Tuples ----

# Write a program that:

# Generates a list of 10 tuples, each tuple consisting of 3 random integers between 1 and 100
# Sorts the list of tuples in increasing order of the third element in each tuple
# Prints the sorted list of tuples
# For example, if the generated input list is:
# [(56, 77, 69), (43, 30, 38), (2, 77, 101), (93, 57, 4), (74, 21, 77),
# (39, 68, 68), (65, 53, 96), (16, 29, 88), (88, 70, 38)]
# The output should be: [(93, 57, 4), (43, 30, 38), (88, 70, 38), (39, 68, 68), (56, 77, 69), (74, 21, 77),
# (16, 29, 88), (65, 53, 96), (2, 77, 101)]

import random
tuplist = []
i = 0
x = 0
dummy_tuple = [0, 0, 0]

for i in range(10):
    for x in range(3):
        dummy_tuple[x] = random.randrange(1, 100)
        x += 1
    new_tuple = tuple(dummy_tuple)
    tuplist.append(new_tuple)
print(f"My input list is as follows: \n{tuplist}")

tuplist_sorted = sorted(tuplist, key = lambda tup:tup[2])

print(f"This is the list when sorted by the third item of each tuple:\n{tuplist_sorted}")
