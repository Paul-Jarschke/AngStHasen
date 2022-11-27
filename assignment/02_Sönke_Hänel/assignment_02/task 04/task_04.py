# Task 04 – Sorted List of Tuples
#
# Write a program that:
#
#     Generates a list of 10 tuples, each tuple consisting of 3 random integers between 1 and 100
#     Sorts the list of tuples in increasing order of the third element in each tuple
#     Prints the sorted list of tuples
#
# For example, if the generated input list is:
# [(56, 77, 69), (43, 30, 38), (2, 77, 101), (93, 57, 4), (74, 21, 77), (39, 68, 68), (65, 53, 96), (16, 29, 88), (88, 70, 38)]
# The output should be:
# [(93, 57, 4), (43, 30, 38), (88, 70, 38), (39, 68, 68), (56, 77, 69), (74, 21, 77), (16, 29, 88), (65, 53, 96), (2, 77, 101)]
#
# Hint: You are allowed and encouraged to use built-in functions, such as sorted(), for this task.

import random

# initialize empty list
mylist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# fill list
for x in range(10):
    mylist[x] = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100))

mylist_sorted = sorted(mylist, key=lambda tup: tup[2])

# printing of sorted list
print(mylist_sorted)
