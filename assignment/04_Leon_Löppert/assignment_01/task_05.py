################################################
#### Programing for Data Scientists: Python ####
####              Assignment 01             ####
####             by Leon Löppert            ####
################################################

# Task 05 - Triangle Checking ----

# Write a Python program that asks the user to input the lengths of the sides in a triangle and outputs
# whether the triangle is equilateral, isosceles, or scalene.
# The program should also check for the Triangle inequality  (z<x+y) , and prompt the user for a valid input.

# An equilateral triangle is a triangle in which all three sides are of equal length.
# An isosceles triangle is a triangle with (at least) two sides of equal length.
# A scalene triangle is a triangle in which all three sides have different lengths.
# For example, if the user inputs a=3, b=4, c=5, the triangle is scalene.

def main():
    a = float(input("How long is side a?\n"))
    b = float(input("How long is side b?\n"))
    c = float(input("How long is side c?\n"))

    if a <= 0 or b <= 0 or c <= 0:
        print("Your triangle is not valid. Please enter valid side lengths.")
        main()
    elif a + b < c or a + c < b or b + c < a:
        print("Your triangle is not valid. Please enter valid side lengths.")
        main()
    elif a == b == c:
        print("Your triangle is equilateral!")
    elif a != b != c:
        print("Your triangle is scalene!")
    else:
        print("Your triangle is isosceles!")

main()
