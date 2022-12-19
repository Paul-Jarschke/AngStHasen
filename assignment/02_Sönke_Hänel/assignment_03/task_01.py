"""Task 01 – Dictionary

Imagine you have to write a (very simple) bookkeeping system for a bank that keeps track of the account balances of each of its customers.
    1. Write a function that spans a dictionary holding a default balance of 0 for an initial list of customers.
    2. What are elegant ways to add or remove single and multiple customers using the functionality of dict?
    3. Now write two simple functions that allow you to deposit and withdraw money for a given bank customer.
    4. Include error messages for inputs that are not permissible, e.g., withdrawing negative amounts or overdrawing the account, etc."""


# 1. Write a function that spans a dictionary holding a default balance of 0 for an initial list of customers.
# For simplicity, assume customer names are unique identifier.
# (optional) Can you express that same functionality using a lambda function?

def create_balance(customer_list=[]):
    balance = {}
    for customer in customer_list:
        balance[customer] = 0
    return balance


# 2. What are elegant ways to add or remove single and multiple customers using the functionality of dict?

# removing (i. single, ii. multiple, iii. all) elements
"""
i.    remove a single element by del balance[customer]
 
ii.   remove multiple elements by iterating over the keys in the dictionary (see lecture: Mutate), f.e.:
"""
# delete every account of a person that start with T:
#     def delete_start_with_t(balance):
#         temp_book = balance.copy()
#         for customer in balance:
#             if customer[0] in "tT":
#                 del temp_book[customer]
#         return temp_book
#
#     test_book = create_balance(["Yildirim", "Thorsten,", "Takyon", "Akira"])
#     test_book = delete_start_with_t(test_book)
#     print(test_book)
#
"""
iii.   all elements by balance.clear()
"""
# adding (i. single, ii. multiple) elements
"""
i.   add an account and balance by setting the value in the account corresponding to the new key to the balance, f.e.:
#       test_book["Sönke"] = 3.50
#       
ii.  adding multiple elements by zipping:
"""


# #ZIP
# names = ['Jan', 'Leon', 'Paul']
# moneys = [12345, 99999, 25000]
# for n, m in zip(names, moneys):
#     test_book[n] = m

# 3. Now write two simple functions that allow you to deposit and withdraw money for a given bank customer.
# 4. including error messages.

def deposit(amount, balance, customer):
    if amount > 0:
        balance[customer] += amount
    else:
        print("You can't deposit a non-positive amount!\n")


def withdraw(amount, balance, customer):
    if amount <= 0:
        print("Error! Tried to withdraw a non-positive amount!\n")
    elif amount > balance[customer]:
        print("Error! Tried to withdraw more money than is deposited!\n")
    else:
        balance[customer] -= amount

# just to test
test_book = create_balance(["Yildirim", "Thorsten,", "Takyon", "Akira"])
print(test_book)
