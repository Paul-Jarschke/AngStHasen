# Task 05 – Check Brackets
#
# Write a program that reads in a string, which is supposed to be a mathematical expression.
# Focus on brackets only and check whether left and right brackets are composed correctly.
# Ignore all other characters (i.e. you don’t have to check correctness of operators and operands).
# Examples of correct input:
#
#     3*(2+5)
#     ((()())())
#     (3+)(((4)))
#     Empty string
#
# Examples of incorrect input:
#
#     (3*(2+5)
#     ((()())(())
#     (3+)((4)))
#     ())(()

string_input = input("Please enter a mathematical expression!\n")

# a counter for how many brackets need to be closed
# notice: you can always open another bracket, but you need to close it in the end
# however, if you close a bracket before you opened one, it's a syntax error
# hence: if bracket_to_close drops BELOW 0 EVEN ONCE, it's over
bracket_to_close = 0

is_valid_input = True
# flag for checking if the input is acceptable

for char in string_input:
    if char == '(':
        bracket_to_close += 1
    if char == ')':
        bracket_to_close -= 1
    is_valid_input &= bracket_to_close >= 0
if bracket_to_close != 0:
    is_valid_input = False

print(is_valid_input)
