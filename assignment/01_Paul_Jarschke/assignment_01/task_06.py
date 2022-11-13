# Task 6
# Write a program that reads a non-negative integer number in the decimal representation provided by the user and prints
# the octal representation of the number. For example, if the user enters 167, the output should be 247.

int_dec = int(input('Please enter a non-negative number (integer) that should be converted into the octal system\n'))

int_oct = ''
div = 2     # 2 resembles arbitrary value >= 1 to start loop

while div >= 1:
    i = int(int_dec % 8)
    div = int_dec / 8
    int_dec = div
    int_oct = str(i) + int_oct

print(int_oct)

# Write a more general program that reads in a non-negative number (potentially including decimal places) in the decimal
# representation provided by the user and prints the octal representation of the number. For example, if the user enters
# 25.11, the output should be 31.0702436560507534.

float_dec = float(input('Please enter a non-negative number (float) that should be converted into the octal system\n'))
