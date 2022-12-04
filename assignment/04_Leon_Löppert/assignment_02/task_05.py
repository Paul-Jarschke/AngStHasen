################################################
#### Programing for Data Scientists: Python ####
####              Assignment 02             ####
####             by Leon Löppert            ####
################################################

# Task 05 – Check Brackets ----

# Write a program that reads in a string, which is supposed to be a mathematical expression.
# Focus on brackets only and check whether left and right brackets are composed correctly.
# Ignore all other characters (i.e. you don’t have to check correctness of operators and operands).
#
# Examples of correct input:
# 3*(2+5)
# ((()())())
# (3+)(((4)))
# Empty string

# Examples of incorrect input:
# (3*(2+5)
# ((()())(())
# (3+)((4)))
# ())(()

eq = str(input("Give me an equation, please:\n"))

left_count = 0
right_count = 0

for letter in eq:
    if letter == "(":
        left_count += 1
    if letter == ")":
        right_count += 1
    if right_count > left_count:
        correct = False
        break

correct = True if left_count == right_count else False

if correct:
    print("Equation is correctly specified.")
else:
    print("Something went wrong. Check if you're missing a bracket.")
