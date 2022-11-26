# Task 04 - Sorted List of Tuples
# Write a program that:
#
#     Generates a list of 10 tuples, each tuple consisting of 3 random integers between 1 and 100
#     Sorts the list of tuples in increasing order of the third element in each tuple
#     Prints the sorted list of tuples
#
# For example, if the generated input list is: [(56, 77, 69), (43, 30, 38), (2, 77, 101), (93, 57, 4), (74, 21, 77),
# (39, 68, 68), (65, 53, 96), (16, 29, 88), (88, 70, 38)]
# The output should be: [(93, 57, 4), (43, 30, 38), (88, 70, 38), (39, 68, 68), (56, 77, 69), (74, 21, 77), (16, 29, 88)
# , (65, 53, 96), (2, 77, 101)]
#
# Hint: You are allowed and encouraged to use built-in functions, such as sorted(), for this task.
import random


def tuple_generator(range_min=1, range_max=100, n_tup=10, tuple_length=3, lst=None):
    """Generating a list with n_tup tuples.
       Each tuple holds tuple-length number of random integer between range_min and range_max. """
    if lst is None:
        lst = []
    for _ in range(n_tup):
        tup = tuple([random.randint(range_min, range_max) for _ in range(tuple_length)])
        lst.append(tup)
    return lst


##############
# Solution 1 #
##############

# generate
list_of_tuples = tuple_generator()
# using own function to access third value in
sorted_by_third = sorted(list_of_tuples, key=lambda tup: tup[2])

# print unsorted and sorted list
print(f'Solution 1')
print(f'List of tuples:\n{list_of_tuples}')
print(f'List of tuples sorted:\n{sorted_by_third}')
print('\n')

##############
# Solution 2 #
##############
from operator import itemgetter


list_of_tuples = tuple_generator()
# using itemgetter to access third values in each tuple
# this approach is more efficient/faster, than using a lambda function
sorted_by_third = sorted(list_of_tuples, key=itemgetter(2))

# print unsorted and sorted list
print(f'Solution 2')
print(f'List of tuples:\n{list_of_tuples}')
print(f'List of tuples sorted:\n{sorted_by_third}')
