# Task 01 - Lambda functions

# Python supports lambda functions as a handy way to define small, anonymous, i.e., unnamed, functions inline.
# Use a lambda function only to retain the even values in an array of integers. Test your function with an input array
# of your choosing. Print the input array and the filtered output array to stdout.

import numpy as np

# input to numpy.array
array = np.array(list(map(int, input("Please enter a number of integers and separate them by pressing space:\n").split())))
print(f'Your array of integers:\n{array}')

# filter array for even values
array = np.array(list(filter(lambda x: (x % 2 == 0), array)))
print(f'Filtered array with even integers:\n{array}')
