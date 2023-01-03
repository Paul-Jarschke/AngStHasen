################################################
#### Programing for Data Scientists: Python ####
####              Assignment 04             ####
####             by Leon Löppert            ####
################################################

# Task 01 - Lambda functions ----

# Use a lambda function only to retain the even values in an array of integers.
# Test your function with an input array of your choosing. Print the input array
# and the filtered output array to stdout.

import numpy as np

array = np.array([[1, 2, 3, 4], \
                  [5, 6, 7, 8]])
print('The input array is:\n', array, sep = '')

result = (lambda l: l[l % 2 == 0])(array)

print('\nThe filtered output array is:\n', result, sep = '')
