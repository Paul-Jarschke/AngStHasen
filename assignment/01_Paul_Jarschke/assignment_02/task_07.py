# Task 07 - Queue
# Write a program that simulates a queue. It will read strings from the input. Consider these inputs as names of people
# coming to the end of a queue. Whenever “next” is given as input, the program will print out the name on the turn.
# The program finishes as soon as the queue is empty.

stack = []

while True:
    # input name
    expression = input('Please enter a name that should be added to the queue, or type "next".\n')

    if expression == 'next':
        # pop item in front of queue
        turn = stack.pop(0)
        print(f'It is your turn {turn}!')
        print(f'Remaining Queue: {stack}')

        if stack == []:
            # stop if queue
            print('The queue is finally empty!')
            break
    else:
        # put name at the end of the stack
        stack.append(expression)
        print(f'Current Queue: {stack}')


