# Task 06 - Check Brackets (2)
# Extend previous program, so it can handle also square and curly brackets. Note that expressions in brackets cannot
# overlap. So, expression {[()()]([[]])}{} is correct, but expression ([)] is not.

expression = input('Please enter a mathematical expression:\n')


def bracket_strip(string):
    """Extracts all brackets from a given string and .
    :param string: string that should be stripped from everything but its brackets
    :return: stripped (str): a new variable that hold just the brackets from th input string
    """
    # initiate var with relevant bracket and empty string
    brackets = '()[]{}'
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

    # initialize dictionary with all sorts of brackets
    bracket_dict = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for i in string:

        # push opening bracket to stack
        # every opening! bracket in the input string is added to the stack
        # therefore we do not need to strip the input string before we apply the function to it
        if i in bracket_dict.keys():
            stack.append(i)
        else:

            # closing bracket without matching opening bracket
            # if there is a closing bracket in the input but the stack is empty, then there was no opening bracket
            if stack == []:
                return False

            # if closing bracket -> pop top item in stack (which should be an opening bracket)
            # if an opening bracket already exists in the stack, then
            open_bracket = stack.pop()

            # not matching bracket -> INVALID
            # since every closing bracket leads to the last opening bracket being popped from the stack, we have to
            # check if the popped opening bracket and the opening bracket at index i are of the sam kind.
            # if the popped opening bracket does not match the kind of opening index at index i, then the bracket
            # structure is incorrect
            if i != bracket_dict[open_bracket]:
                return False

    # check if stack is empty -> True if there are no opening brackets without closing brackets
    return stack == []


# declare var for validity check of stripped input
check = is_valid(bracket_strip(expression))
print(f'The constellation of brackets is valid: {check}')
