"""Task 02 – Classes

The manager thinks that the simple bookkeeping system you have built is not powerful enough. She requests that you start from scratch and use classes instead.

    1.  Write a simple class with appropriate constructor __init__ that initializes an object of class Customer tracking the same information as in Task 01.
    2.  Now write two simple methods for class Customer that allow you to deposit and withdraw money for a given customer object.
    3.  Include error messages for inputs that are not permissible, e.g., withdrawing negative amounts or overdrawing the account.
    4.  (Inheritance) Write a child class SavingsCustomer that inherits its features from the parent class Customer.
        A savings customer has an extra savings balance for receiving extra interest.
        The class should have a method to transfer money back and forth between the accounts' main balance as well as the savings balance. Do not forget to add reasonable error messages.
"""


class Customer:
    """A simple attempt to represent bookkeeping."""

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    """A function that lets you deposit any non-negative amount in the bank"""

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("You can't deposit a non-positive amount!\n")

    """A function that lets you withdraw any non-negative amount from the bank, if enough money is deposited"""

    def withdraw(self, amount):
        if amount <= 0:
            print("Error! Tried to withdraw a non-positive amount!\n")
        elif amount > self.balance:
            print("Error! Tried to withdraw more money than is deposited!\n")
        else:
            self.balance -= amount


class SavingsCustomer(Customer):
    """A child class SavingsCustomer that inherits its features from the parent class Customer."""
    savings = 0

    def transfer_to_savings(self, amount):
        if amount <= 0:
            print("Error! Tried to transfer a non-positive amount!\n")
        elif amount > self.balance:
            print("Error! Tried to withdraw more money than is deposited!\n")
        else:
            self.balance -= amount
            self.savings += amount

    def transfer_from_savings(self, amount):
        if amount <= 0:
            print("Error! Tried to transfer a non-positive amount!\n")
        elif amount > self.savings:
            print("Error! Tried to withdraw more money than is deposited!\n")
        else:
            self.balance += amount
            self.savings -= amount


# """Code for Testing. Uncomment to test the class"""
# s = SavingsCustomer("Sönke", 420)
# print(str(s.name), str(s.balance), str(s.savings))
# s.deposit(420)
# print(str(s.name), str(s.balance), str(s.savings))
# s.transfer_to_savings(421)
# print(str(s.name), str(s.balance), str(s.savings))
# s.transfer_from_savings(421)
# print(str(s.name), str(s.balance), str(s.savings))
# s.transfer_to_savings(140)
# print(str(s.name), str(s.balance), str(s.savings))
# s.transfer_to_savings(140)
# print(str(s.name), str(s.balance), str(s.savings))
# s.transfer_to_savings(140)
# print(str(s.name), str(s.balance), str(s.savings))
# s.transfer_to_savings(140)
# print(str(s.name), str(s.balance), str(s.savings))
# s.transfer_to_savings(140)
# print(str(s.name), str(s.balance), str(s.savings))
# s.transfer_to_savings(140)
# print(str(s.name), str(s.balance), str(s.savings))
# s.transfer_to_savings(140)
# print(str(s.name), str(s.balance), str(s.savings))
#
# s.transfer_to_savings(0)
# print(str(s.name), str(s.balance), str(s.savings))
