# ## Task 05 –Triangle Checking
# Write a Python program that asks the user to input the lengths of the sides in a triangle and
# outputs whether the triangle is equilateral, isosceles, or scalene.
# The program should also check for the Triangle inequality(𝑧<𝑥+𝑦), and prompt the user for a valid input.
# •An equilateral triangle is a triangle in which all three sides are of equal length.
# •An isosceles triangle is a triangle with (at least) two sides of equal length.
# •A scalene triangle is a triangle in which all three sides have different lengths.
#  For example, if the user inputs a=3, b=4, c=5, the triangle is scalen

# initializing values
a = 0
b = 0
c = 1

# check for possible data input (does not explicitly check for non-negativity though)
while a > b + c or b > a + c or c > a + b:
    print("Please enter valid inputs for the sides of the triangle.")
    a = int(input("Provide a length for side a (number) please.\n"))
    b = int(input("Provide a length for side b (number) please.\n"))
    c = int(input("Provide a length for side c (number) please.\n"))

# check if equilateral
if (a == b) and (b == c):
    print("The triangle is equilateral")
# check if at least isosceles
elif (a == b) or (b == c) or (a == c):
    print("The triangle is isosceles")
else:
    print("The triangle is scalene, bummer")
