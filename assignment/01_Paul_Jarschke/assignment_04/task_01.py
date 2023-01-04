# Task 01 - Lambda functions

# Python supports lambda functions as a handy way to define small, anonymous, i.e., unnamed, functions inline.
# Use a lambda function only to retain the even values in an array of integers. Test your function with an input array
# of your choosing. Print the input array and the filtered output array to stdout.

# input to list
lst = list(map(int, input("Please enter an arbitrary number of integers and separate them by pressing space:\n").split()))
print(f'Your list of integers:\n{lst}')

# filter list for even values
lst = list(filter(lambda x: (x % 2 == 0), lst))
print(f'Filtered list with even integers:\n{lst}')
