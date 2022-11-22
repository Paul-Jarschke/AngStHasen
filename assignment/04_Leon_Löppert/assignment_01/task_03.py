################################################
#### Programing for Data Scientists: Python ####
####              Assignment 01             ####
####             by Leon Löppert            ####
################################################

# Task 03 - Fibonacci Numbers ----

# Write a program that reads in an upper bound (number) provided by the user and
# prints the sequence of Fibonacci numbers that are less or equal to the number given by the user.
# Use a while-loop for this task.The Fibonacci sequence is defined as F_n = F_(n-1) + F_(n-2).
# Use F_0 = 0 and F_1 = 1 as seed values. For example, if the user inputs 6, the output should be 0, 1, 1, 2, 3, 5.

F0 = 0
F1 = 1
Flist = [F0, F1]
upbound = int(input("Give me an upper bound: \n")) # upper bound

n = 3
i = 2
while n <= upbound:
    Fn = 0
    newvalue = Flist[i-1] + Flist[i-2]
    Flist.append(newvalue)
    i = i + 1
    n = n + 1
print(Flist)
