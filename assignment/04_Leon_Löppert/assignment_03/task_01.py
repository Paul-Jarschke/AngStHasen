################################################
#### Programing for Data Scientists: Python ####
####              Assignment 03             ####
####             by Leon Löppert            ####
################################################

# Task 01 - Dictionary ----

# Imagine you have to write a (very simple) bookkeepingsystem for a bank that keeps track of the account balances of each of its customers.
#
# Write a function that spans a dictionary holding a default balance of 0 for an initial list of customers.
# For simplicity, assume customer names are unique identifier.
# (optional) Can you express that same functionality using a lambda function?

# What are elegant ways to add or remove single and multiple customers using the functionality of dict?
# Now write two simple functions that allow you to deposit and withdraw money for a given bank customer.
# Include error messages for inputs that are not permissible, e.g., withdrawing negative amounts or overdrawing the account, etc.

# Initialize banking system and customer list
def initialize_banking():
    customer_list = []

    customer_name = input("Give me the name of a customer I should append to the list of initial customers:\n")

    if customer_name == "":
        "Please try again:"
    else:
        customer_list.append(customer_name)

    while customer_name != "":
        customer_name = input("Give me another customer's name or press 'Enter' if no more customer should be added:\n")
        customer_list.append(customer_name)

    customer_list.pop(-1)

    length = len(customer_list)
    balances = [0] * length
    banking = dict(zip(customer_list, balances))
    return banking

system1 = initialize_banking()

# Remove one or multiple customers from dictionary
remove = ['name1', 'name2']
[system1.pop(c) for c in remove]

# Add one or multiple customers to dictionary
add = ['name1', 'name2']
system2 = {newc: 0 for newc in add}
system1.update(system2)

# Function to deposit money to a customer in arbitrary banking system
def deposit(banking, customer, amount):
    if type(customer) != str or customer not in banking.keys():
        print('Not a valid customer! Try again.')
    elif type(amount) != (int or float):
        print('Not a valid number to deposit! Try again.')
    elif amount <= 0:
        print('Not a valid number to deposit! Try again.')
    else:
        banking[customer] += amount

# Function to withdraw money to a customer in arbitrary banking system
def withdraw(banking, customer, amount):
    if type(customer) != str or customer not in banking.keys():
        print('Not a valid customer! Try again.')
    elif type(amount) != (int or float):
        print('Not a valid number to withdraw! Try again.')
    elif amount <= 0:
        print('Not a valid number to withdraw! Try again.')
    elif (banking[customer] - amount) < 0:
        print('You can not overdraw your account! Try again with a lower amount.')
    else:
        banking[customer] -= amount
