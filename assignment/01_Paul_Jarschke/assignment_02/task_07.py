# Task 07 - Queue
# Write a program that simulates a queue. It will read strings from the input. Consider these inputs as names of people
# coming to the end of a queue. Whenever “next” is given as input, the program will print out the name on the turn.
# The program finishes as soon as the queue is empty.

# Since we start with an empty queue, we can not break the program before the user is able to enter something.
# I chose to break the loop in two different scenarios:
# 1) No Person was ever added to the queue and the first input is "next"
# 2) The last person is removed from the list.

# initiate empty list resembling the queue
stack = []

while True:
    # input name
    expression = input('Please enter a name that should be added to the queue, or type "next".\n')

    if expression == 'next':

        if not stack:
            # stop if queue is empty
            print('The queue is empty. Goodbye!')
            break
        # pop item in front of queue
        turn = stack.pop(0)
        print(f'It is your turn {turn}!')

        if not stack:
            # stop if queue is empty
            print('The queue is empty. Goodbye!')
            break
        else:
            print(f'Remaining Queue: {stack}')

    else:
        # put name at the end of the stack
        stack.append(expression)
        print(f'Current Queue: {stack}')
