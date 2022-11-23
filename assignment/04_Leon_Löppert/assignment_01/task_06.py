################################################
#### Programing for Data Scientists: Python ####
####              Assignment 01             ####
####             by Leon Löppert            ####
################################################

# Task 06 - Decimal to Octal conversion ----

# a) Write a program that reads a non-negative integer number in the decimal representation provided by the user and
# prints the octal representation of the number. For example, if the user enters 167, the output should be 247.

# b) Write a more general program that reads in a non-negative number (potentially including decimal places) in the
# decimal representation provided by the user and prints the octal representation of the number.
# For example, if the user enters 25.11, the output should be 31.0702436560507534.

# a) Only non-negative integers

#def main_a():
#    nni = input("Type in non-negative integer number in decimal representation: \n")
#
#    test = bool(True)
#    try:
#        int(nni)
#    except ValueError:
#        test = bool(False)
#
#
#    if not test: # Not valid when float
#        print("Not a valid number. Try again.")
#        main_a()
#    nni = int(nni)
#    if nni < 0: # Not valid when negative
#        print("Not a valid number. Try again.")
#        main_a()
#
#    octa = str(oct(nni))
#    octa = octa.replace("0o", "")
#    print("Converted to octal representation your number equals:\n", octa, sep = "")
#
#main_a()

# b) non-negative number (potentially including decimal places)


def main_b():

    nnn = input("Type in arbitrary non-negative number in decimal representation: \n")

    # separate into whole and decimal places
    whole, dec = str(nnn).split(".")

    separator = int(dec)
    leadingzero = len(dec.split(str(separator), 1)[0])

    dec = int(dec)
    whole = int(whole)
    length = len(str(dec))


    #octwhole = oct(whole).lstrip("0o")
    octwhole = oct(whole).replace("0o", "")

    i = 0
    octdec = [""]
    while i < 16:
        newdec, dec = str(dec/(10**(length+leadingzero)) * 8).split(".")
        octdec.append(newdec)
        dec = int(dec)
        i = i + 1

    jointdec = "".join(octdec)
    result = str(octwhole) + "." + jointdec
    print("The resulting octal representation is: \n", result, sep = "")

main_b()
