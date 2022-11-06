# ## Task 06 –Decimal to Octal Conversion
# Write a program that reads a non-negative integer number in the decimal representation provided by the user
# and prints the octal representation of the number. For example, if the user enters 167, the output should be 247.
# a.Write a more general program that reads in a non-negative number (potentially including decimal places)
# in the decimal representation provided by the user and prints the octal representation of the number.
# For example, if the user enters 25.11, the output should be 31.0702436560507534.

# user input. make sure to only accept non-negative integers.
input_integer = -1
while input_integer < 0:
    input_integer = int(input("Provide a non-negative integer number in the decimal representation please.\n"))

# initialize empty string
octal_string = ""

# As long as the number is not 0,
# remainder of the division of the number by 8 is the next (bigger) octal potency.
# the number without remainder by 8 and continue with the next octal digit.
while input_integer != 0:
    octal_string = str(input_integer % 8) + octal_string
    input_integer = input_integer // 8

# output
print(octal_string)
