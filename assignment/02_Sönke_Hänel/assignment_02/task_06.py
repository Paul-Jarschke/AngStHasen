# Task 06 – Check Brackets II
#
# Extend previous program, so it can handle also square and curly brackets.
# Note that expressions in brackets cannot overlap.
# So, expression {[()()]([[]])}{} is correct, but expression ([)] is not.

string_input = input("Please enter a mathematical expression!\n")

# a respective counter for how many brackets need to be closed - one for each kind of brackets
# notice: you can always open another bracket, but you need to close it in the end
# however, if you close a bracket before you opened one, it's a syntax error
# hence: if bracket_to_close drops BELOW 0 EVEN ONCE, it's over

curly_brackets_to_close = 0
square_brackets_to_close = 0

# flag for checking if the input is acceptable
is_valid_input = True

# keep track of in which order brackets need to be closed by adding a support-string
helper_string = ""

for char in string_input:
    if char == '(':
        curly_brackets_to_close += 1
        helper_string = ")" + helper_string
    if char == ')':
        curly_brackets_to_close -= 1
        if helper_string[0] != ')':
            is_valid_input = False
        helper_string = helper_string[1:]

    if char == '[':
        square_brackets_to_close += 1
        helper_string = "]" + helper_string
    if char == ']':
        square_brackets_to_close -= 1
        if helper_string[0] != ']':
            is_valid_input = False
        helper_string = helper_string[1:]
    is_valid_input &= curly_brackets_to_close >= 0

if curly_brackets_to_close != 0 | square_brackets_to_close != 0:
    is_valid_input = False
print(is_valid_input)
