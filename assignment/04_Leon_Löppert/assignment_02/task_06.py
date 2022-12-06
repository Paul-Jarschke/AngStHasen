################################################
#### Programing for Data Scientists: Python ####
####              Assignment 02             ####
####             by Leon Löppert            ####
################################################

# Task 06 – Check Brackets II ----

# Extend previous program, so it can handle also square and curly brackets.
# Note that expressions in brackets cannot overlap.
# So, expression {[()()]([[]])}{} is correct, but expression ([)] is not.


eq = str(input("Give me an equation, please:\n"))

bracket_dict = {"(": 0, ")": 0, "[": 0, "]": 0, "{": 0, "}" : 0}
correct = True
expected_close = []

for letter in eq:
    if letter in ["(", ")", "[", "]", "{", "}"]:
        bracket_dict[letter] += 1
    if letter == "(":
        expected_close.insert(0, ")")
    elif letter == "[":
        expected_close.insert(0, "]")
    elif letter == "{":
        expected_close.insert(0, "}")
    if bracket_dict["("] < bracket_dict[")"]:
        correct = False
        break
    if bracket_dict["["] < bracket_dict["]"]:
        correct = False
        break
    if bracket_dict["["] < bracket_dict["]"]:
        correct = False
        break

    if letter in [")", "]", "}"] and letter != expected_close[0]:
        correct = False
        break
    elif letter in  [")", "]", "}"] and letter == expected_close[0]:
        expected_close.pop(0)

if bracket_dict["("] != bracket_dict[")"]:
        correct = False
if bracket_dict["["] != bracket_dict["]"]:
        correct = False
if bracket_dict["{"] != bracket_dict["}"]:
        correct = False


if correct:
    print("Equation is correctly specified.")
else:
    print("Something went wrong. Check if you're missing a bracket.")

