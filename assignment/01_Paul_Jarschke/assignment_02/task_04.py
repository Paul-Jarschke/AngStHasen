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


# this code is still trash :/
def tuple_generator(range_min=1, range_max=100, n_tuples=2, tuple_length=3, lst=[], lst2=[]):
    for _ in range(n_tuples):
        for _ in range(tuple_length):
            num = random.randint(range_min, range_max)
            print(num)
            lst.append(num)
            print(lst)
            tup = tuple(lst)
        lst2.append(tup)
    return lst2


print(f'function call{tuple_generator()}')
