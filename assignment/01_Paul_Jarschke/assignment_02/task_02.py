# Task 02 - Largest List Element
# Write a program that generates a list of 10 random integers between 1 and 100 and then finds and prints the largest
# element in the list. Do not use the built-in function max(). For example, if the input is [23,3,42,29,12,15,8,4,37,34]
# , the output should be the largest element: 42.

# import random module to generate random integers
import random

###############
# Solution 01 #
###############


# function that creates a list of random integers (by default 10 integers between 1 and 100)
def random_numbers(range_min=1, range_max=100, n=10, lst=None):
    if lst is None:
        lst = []
    for _ in range(n):
        num = random.randint(range_min, range_max)
        lst.append(num)
    return lst


print('Solution 01:')

# generation via function
nums = random_numbers()
print(f'Your randomly generated list:\n{nums}')

# sort in ascending order
nums = sorted(nums)
print(f'The largest value:\n{nums[-1]}\n')


###############
# Solution 02 #
###############

print('Solution 02:')

# generation via list comprehension
list_comp = [random.randint(1, 100) for x in range(10)]
print(f'Your randomly generated list:\n{list_comp}')

# sort in ascending order
list_comp = sorted(list_comp)
print(f'The largest value:\n{list_comp[-1]}')
