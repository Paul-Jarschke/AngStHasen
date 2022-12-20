# Task 01 - Dictionary

# Imagine you have to write a bookkeepingsystem for a bank that keeps track of the account balances of each of its customers.
# Write a function that spans a dictionary holding a default balance of 0 for an initial list of customers.
# For simplicity, assume customer names are unique identifier.
# (optional) Can you express that same functionality using a lambda function?
# What are elegant ways to add or remove single and multiple customers using the functionality of dict?
# Now write two simple functions that allow you to deposit and withdraw money for a given bank customer.
# Include error messages for inputs that are not permissible,
# e.g., withdrawing negative amounts or overdrawing the account, etc.


# Functions
# dictionary spanning
def create_book(names=[]):
    """Creates a dictionary."""
    dictionary = {}
    for item in names:
        dictionary[item] = 0
    return dictionary


def deposit(customer, value):
    """Adds value to a specific account."""
    if customer not in cust:
        print(f'This person has no account.')
    elif type(value) != int and type(value) != float:
        print('You can only enter numerical values!')
    elif value < 0:
        print('You cannot deposit negative amounts!')
    else:
        book[customer] += value
    print(f'Book after deposition:\n{book}')


def withdraw(customer, value):
    """Decreases value of a specific account."""
    if customer not in cust:
        print(f'This person has no account.')
    elif type(value) != int and type(value) != float:
        print('You can only enter numerical values!')
    elif value < 0:
        print('You cannot withdraw negative amounts!')
    elif value > book[customer]:
        print(f'{customer} does not have enough money in his/her bank account! '
              f'You can only withdraw up to {book[customer]}$.')
    else:
        book[customer] += -value
    print(f'Book after withdrawal:\n{book}')


# initial list of customers
cust = ['Paul', 'Leon', 'Laura', 'Jan']

# create a book for given names (cust)
book = create_book(names=cust)
print(f'This is your new book:\n{book}')

# deposit a positive value
print('\nTask: 100$ deposit for Paul')
deposit('Paul', 100)

# deposit a negative value
print('\nTask: -100$ deposit for Paul')
deposit('Paul', -100)

# withdraw a positive amount
print('\nTask: 50$ withdrawal for Paul')
withdraw('Paul', 50)

# withdraw a negative amount
print('\nTask: -50$ withdrawal for Paul')
withdraw('Paul', -50)

# try to withdraw an unavailable amount of money
print('\nTask: 1000000$ withdrawal for Paul')
withdraw('Paul', 1000000)

# name not in cust (deposit)
print('\nTask: 1$ deposit for Simon')
deposit('Simon', 1)

# non-numerical input (deposit)
print('\nTask: 1$ deposit for Paul')
deposit('Paul', 'money')

# name not in cust (withdrawal)
print('\nTask: 1$ withdrawal for Simon')
withdraw('Simon', 1)

# non-numerical input (withdrawal)
print('\nTask: 1$ withdrawal for Paul')
withdraw('Paul', 'money')


# Question:
# What are elegant ways to add or remove single and multiple customers ?

# Answer:
# You can remove an item with pop() or delete it completely with del(). Popitem() removes that last added item
# With clear() you can clear the whole dictionary.
# Using dict["key"] = "item" or you can merge 2 dictionaries using update()
# You could also use a more complex comprehension like this:
# final_dict = {key: value for key, value in d if key not in [key1, key2]}
