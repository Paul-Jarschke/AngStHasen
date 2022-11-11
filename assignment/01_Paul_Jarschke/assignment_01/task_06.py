# Task 6
# Write a program that reads a non-negative integer number in the decimal representation provided by the user and prints
# the octal representation of the number. For example, if the user enters 167, the output should be 247.

num_dec = int(input('Please enter a non-negative number that should be converted into the octal system\n'))
num_dec = str(num_dec)

num_oct = ''
for i in num_dec:
    octal = (i+1)*8**i
    num_oct += octal

print(num_dec)

# Write a more general program that reads in a non-negative number (potentially including decimal places) in the decimal
# representation provided by the user and prints the octal representation of the number. For example, if the user enters
# 25.11, the output should be 31.0702436560507534.
