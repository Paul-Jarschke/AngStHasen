# Task 07 – Queue
#
# Write a program that simulates a queue.
# It will read strings from the input.
# Consider these inputs as names of people coming to the end of a queue.
# Whenever “next” is given as input, the program will print out the name on the turn.
# The program finishes as soon as the queue is empty.

# initial input
xs = [input("Please enter the name of the first person entering the queue!\n")]

# prompt for more inputs until the queue is done
while xs:
    x = input("Please enter another name or 'next'!\n")
    if x.lower() == "next":
        print(xs.pop(0))
    # drop empty names
    elif x != '':
        xs.append(x)

### legacy (dont delete yet!) ###
# while xs:
#     xs_2 = (input("Please enter even more names separated by whitespaces or 'next'\n")).split(sep=' ')
#     while xs_2:
#         x = xs_2.pop(0)
#         if x.lower() == "next":
#             print(xs.pop(0))
#         elif x != '':
#             xs.append(x)
#     print(xs)
#     print(xs_2)
