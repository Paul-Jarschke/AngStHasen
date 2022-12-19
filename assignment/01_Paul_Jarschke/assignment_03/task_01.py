# Task 01 - Dictionary

# Imagine you have to write a bookkeepingsystem for a bank that keeps track of the account balances of each of its customers.
#
# Write a function that spans a dictionary holding a default balance of 0 for an initial list of customers.
# For simplicity, assume customer names are unique identifier.
# (optional) Can you express that same functionality using a lambda function?
# What are elegant ways to add or remove single and multiple customers using the functionality of dict?
# Now write two simple functions that allow you to deposit and withdraw money for a given bank customer.
# Include error messages for inputs that are not permissible,
# e.g., withdrawing negative amounts or overdrawing the account, etc.


# initial list of customers
cust = ['Paul', 'Leon', 'Laura', 'Jan']


# 1 dictionary spanning function
def create_book(names=[]):
    book = {}
    for item in names:
        book[item] = 0
    return book


book = create_book(names=cust)
print(book)

# 1 dictionary spanning function (lambda) DOES NOT WORK!
b = lambda people: (dict.fromkeys(item, 0) for item in people)

dictionary = dict.fromkeys(cust, 0)
print(f'\nHier ist das dict {dictionary}')
# 2 elegant ways to add or remove single and multiple customers

# You can remove an item with pop() or delete it completely with del(). Popitem() removes that last added item
# With clear() you can clear the whole dictionary.
# Using dict["key"] = "item" or you can merge 2 dictionaries using update()
# You could also use a more complex comprehension like this:
# final_dict = {key: value for key, value in d if key not in [key1, key2]}

# 3 deposit and withdraw money from customer


def deposit(customer, deposit_amount):
    book[customer] += deposit_amount


def withdraw(customer, withdraw_amount):
    if withdraw_amount < 0:
        print('You cannot withdraw negative amounts.')
    elif withdraw_amount > book[customer]:
        print(f'{customer} does not have enough money in his/her bank account!\nYou can only withdraw up to {book[customer]}$.')
    else:
        book[customer] += -withdraw_amount

# Paul tries to withdraw more money than he has

# Paul deposits 1000 euros
deposit('Paul', 1000)
print(f'New Book:\n{book}')

# Paul
withdraw('Paul', 2000)
print(f'New Book:\n{book}')

