# Task 05 - Check Brackets
# Write a program that reads in a string, which is supposed to be a mathematical expression. Focus on brackets only and
# check whether left and right brackets are composed correctly. Ignore all other characters
# (i.e. you don’t have to check correctness of operators and operands).
# Examples of correct input:
#     3*(2+5)
#     ((()())())
#     (3+)(((4)))
#     Empty string
#
# Examples of incorrect input:
#     (3*(2+5)
#     ((()())(())
#     (3+)((4)))
#     ())(()
expression = input('Please enter a mathematical expression:\n')


def bracket_strip(string=expression):
    """Extracts all round brackets from a string."""

    # initiate var with relevant bracket and empty string
    brackets = '()'
    stripped = ''

    # check string for brackets and add them to a new var: stripped (str)
    for i in string:
        if i in brackets:
            stripped += i
    return stripped


def check_brackets(string=expression):
    """Strip input from everything but round brackets. Check if the """

    # initiate empty lists for opening/closing brackets
    opened = []
    closed = []

    # add
    for _ in string:
        if _ == '(':
            opened.append(_)
        else:
            closed.append(_)
    if len(closed) != len(opened):
        print(f'Your expression is INVALID!')
    else:
        print(f'Your expression is VALID!')


check_brackets(bracket_strip())
