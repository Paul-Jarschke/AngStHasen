# Task 5
# Write a Python program that asks the user to input the lengths of the sides in a triangle and outputs whether the
# triangle is equilateral, isosceles, or scalene. The program should also check for the Triangle inequality (z < x + y),
# and prompt the user for a valid input.

print('Let\'s define the lengths of the sides for a triangle!')

x, y, z = [float(x) for x in input('Please enter 3 numerical values and separate them by pressing space.\n').split()]
lengths = [x, y, z]

# Check for triangle inequality and reject input, until the input is valid
while sum(lengths) <= 2*max(lengths):
    print('Your input does not satisfy the condition for triangle inequality! Please enter a valid set of values.')
    x, y, z = [float(x) for x in input().split()]
    lengths = [x, y, z]

print(f'Length of x: {x} (cm)\nLength of y: {y} (cm)\nLength of z: {z} (cm)\n')

# Check if triangle is equilateral, scalene or isosceles
if x == y == z:
    print('Your triangle is equilateral.')
elif x != y != z:
    print('Your triangle is scalene.')
else:
    print('Your triangle is isosceles.')
