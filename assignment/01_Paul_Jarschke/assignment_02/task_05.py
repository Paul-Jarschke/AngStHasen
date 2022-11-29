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


def bracket_strip(string):
    """Extracts all brackets from a given string and .
    :param string: string that should be stripped from everything but its brackets
    :return: stripped (str): a new variable that hold just the brackets from th input string
    """
    # initiate var with relevant bracket and empty string
    brackets = '()'
    stripped = ''

    # check string for brackets and add them to a new var: stripped (str)
    for i in string:
        if i in brackets:
            stripped += i
    return stripped


def is_valid(string):
    """
    Function that checks if there is a closing bracket for every kind of opening bracket in the input string.
    :param string: string (with brackets, that should be checked for validity)
    :return: boolean
    """
    # len(str) is not even, the constellation of brackets can not be correct -> INVALID
    if len(string) % 2 != 0:
        return False

    # initialize dictionary with brackets
    bracket_dict = {'(': ')'}
    stack = []
    for i in string:

        # push every opening bracket to stack
        if i in bracket_dict.keys():
            stack.append(i)
        else:

            # closing bracket without matching opening bracket -> INVALID
            # if there is a closing bracket in the input but the stack is empty, then there was no opening bracket
            if stack == []:
                return False

            # if closing bracket -> pop top item in stack (opening bracket)
            stack.pop()

    # check if stack is empty: if there are no opening brackets without closing brackets -> VALID
    return stack == []


# apply functions to the input expression
check = is_valid(bracket_strip(expression))
print(f'The constellation of brackets is valid: {check}')
