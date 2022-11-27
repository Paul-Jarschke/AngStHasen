# Task 06 - Check Brackets (2)
# Extend previous program, so it can handle also square and curly brackets. Note that expressions in brackets cannot
# overlap. So, expression {[()()]([[]])}{} is correct, but expression ([)] is not.


def is_valid(test_str):
    # len(test_str) is odd -> invalid!
    if len(test_str) % 2 != 0:
        return False
    # initialize parentheses dict
    par_dict = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in test_str:
        # push opening bracket to stack
        if char in par_dict.keys():
            stack.append(char)
        else:
            # closing bracket without matching opening bracket
            if stack == []:
                return False
            # if closing bracket -> pop stack top
            open_brac = stack.pop()
            # not matching bracket -> invalid!
            if char != par_dict[open_brac]:
                return False
    return stack == []


test = is_valid('{[()()]([[]])}')

print(test)