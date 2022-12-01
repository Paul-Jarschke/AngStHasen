# Write a program that generates a list of 10 random integers between 1 and 100
# and then finds and prints the largest element in the list.
# Do not use the built-in function max().
# For example, if the input is [23,3,42,29,12,15,8,4,37,34],
# the output should be the largest element: 42.
# Hint: Check out the module random.

import random

# get a list of 10 random integers between 1 and 100
mylist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in range(10):
    mylist[x] = random.randint(1, 100)
#    print(mylist[x])

# find the biggest integer in the list
biggest_int = mylist[0]
for x in mylist:
    if x >= biggest_int:
        biggest_int = x
print(biggest_int)
