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


# a. modification

# user input. make sure to only accept non-negative integers.
input_float = -1.0
while input_float < 0:
    input_float = float(input("Provide a non-negative floating point number in the decimal representation please.\n"))

# the idea is to just cut the float into two pieces: the integer part and the part behind the decimal point

# splitting of the two parts:
integer_part = int(input_float)
input_float -= integer_part

# treatment of part before decimal point:

# initialize empty string
octal_string = ""
# As long as the number is not 0,
# remainder of the division of the number by 8 is the next (bigger) octal potency.
# the number without remainder by 8 and continue with the next octal digit.
while integer_part != 0:
    octal_string = str(integer_part % 8) + octal_string
    integer_part = integer_part // 8

# add "octal"point
octal_string = octal_string + "."

# treatment of part after decimal point
# we can run into the problem that we have an eternally repeating sequence of numbers,
# so we specify a maximum of 16 octal places. i is counting these
i = 0

# in each loop multiply the floating point part by 8 and
# take the integer part of the result as the next octal of the number

while input_float != 0.0 and i <= 15:
    input_float *= 8
    integer_part = int(input_float)
    input_float -= integer_part
    octal_string += str(integer_part % 8)
    integer_part = integer_part // 8
    i += 1

# output
print(octal_string)
