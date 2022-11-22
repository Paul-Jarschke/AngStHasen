################################################
#### Programing for Data Scientists: Python ####
####              Assignment 01             ####
####             by Leon Löppert            ####
################################################

# Task 04 - Selective Printing ----

# Write a program that reads in an upper bound (number) provided by the user and prints all integer numbers that are
# less or equal to the upper bound except the integer numbers that are divisible by 3. Use the continue statement.
# For example, if the user enters 6 as the upper bound, the output should be 0, 1, 2, 4, 5.

upperbound = int(input("Give me your upper bound: \n"))
range = range(upperbound)
list = list(range)

def divthree(x):
    if x == 0:
        return(0)
    else:
         return x % 3 == 0

for i in list[:]:
    if divthree(i):
        list.remove(i)

print("Your sequence is: \n ", list)
