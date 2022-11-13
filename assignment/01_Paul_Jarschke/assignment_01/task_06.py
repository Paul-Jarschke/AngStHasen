# Task 6
# Write a program that reads a non-negative integer number in the decimal representation provided by the user and prints
# the octal representation of the number. For example, if the user enters 167, the output should be 247.

num_dec = int(input('Please enter a non-negative number (integer) that should be converted into the octal system\n'))

num_oct = ''
div = 2     # 2 resembles arbitrary value >= 1 to start loop

while div >= 1:
    i = int(num_dec % 8)
    div = num_dec / 8
    num_dec = div
    num_oct = str(i) + num_oct

print(num_oct)

# Write a more general program that reads in a non-negative number (potentially including decimal places) in the decimal
# representation provided by the user and prints the octal representation of the number. For example, if the user enters
# 25.11, the output should be 31.0702436560507534.

num_dec = int(input('Please enter a non-negative number (float) that should be converted into the octal system\n'))