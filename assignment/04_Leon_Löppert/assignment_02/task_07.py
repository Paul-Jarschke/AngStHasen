################################################
#### Programing for Data Scientists: Python ####
####              Assignment 02             ####
####             by Leon Löppert            ####
################################################

# Task 07 – Queue ----

# Write a program that simulates a queue. It will read strings from the input.
# Consider these inputs as names of people coming to the end of a queue.
# Whenever “next” is given as input, the program will print out the name on the turn.
# The program finishes as soon as the queue is empty.

queue = [input("Hello, who's first?\n")]

while queue:
    new = input("Either enter a new person to be added to the queue or 'next'.\n")
    if new == "next":
        call = queue.pop(0)
        print(f"It's your turn, {call}!")
        print("The remaining queue is as follows: " + str(queue).replace("[", "").replace("]", "").replace("'", ""))
    else:
        queue.append(new)
        print("The current queue is as follows: " + str(queue).replace("[", "").replace("]", "").replace("'", ""))


print("The queue is empty.")
