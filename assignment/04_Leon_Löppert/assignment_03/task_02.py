################################################
#### Programing for Data Scientists: Python ####
####              Assignment 03             ####
####             by Leon Löppert            ####
################################################

# Task 02 - Classes ----

# The manager thinks that the simple bookkeeping system you have built is not powerful enough.
# She requests that you start from scratch and use classes instead.

# Write a simple class with appropriate constructor __init__ that initializes an object of class Customer tracking
# the same information as in Task 01.

# Now write two simple methods for class Customer that allow you to deposit and withdraw money for a given customer object.
# Include error messages for inputs that are not permissible, e.g., withdrawing negative amounts or overdrawing the account.
# (Inheritance) Write a child class SavingsCustomer that inherits its features from the parent class Customer.
# A savings customer has an extra savings balance for receiving extra interest.
# The class should have a method to transfer money back and forth between the accounts' main balance as well as the savings balance.
# Do not forget to add reasonable error messages.

class Customer:

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance


    def deposit(self, amount):
        if type(amount) != (int or float):
            print('Not a valid number to deposit! Try again.')
        elif amount <= 0:
            print('Not a valid number to deposit! Try again.')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if type(amount) != (int or float):
            print('Not a valid number to withdraw! Try again.')
        elif amount <= 0:
            print('Not a valid number to withdraw! Try again.')
        elif (self.balance - amount) < 0:
            print('You can not overdraw your account! Try again with a lower amount.')
        else:
            self.balance -= amount


class SavingsCustomer(Customer):
    def __init__(self, name, balance = 0, savings = 0):
        super().__init__(name, balance)
        self.savings = savings

    def transfer(self, direction, amount):
        if direction == "cts":          # checking to savings
            if type(amount) != (int or float):
                print('Not a valid number to transfer! Try again.')
            elif self.balance - amount < 0:
                print('You cannot overdraw your checking account! Try again with a lower amount.')
            elif amount <= 0:
                print('Not a valid number to transfer! Try again.')
            else:
                self.savings += amount
                self.balance -= amount
        elif direction == "stc":        # savings to checking
            if type(amount) != (int or float):
                print('Not a valid number to transfer! Try again.')
            elif self.savings - amount < 0:
                print('You cannot overdraw your savings account! Try again with a lower amount.')
            elif amount <= 0:
                print('Not a valid number to transfer! Try again.')
            else:
                self.savings -= amount
                self.balance += amount
        else:
            print("Not a valid specification for the direction! Type either 'cts' for 'checking to savings or 'stc' for 'savings to checking'.")


# Testing

Tim = Customer('Tim', 0)
Tim = SavingsCustomer('Tim', 0)
Tim.name
Tim.balance

Tim.deposit(20)
Tim.balance
Tim.deposit(-40)
Tim.balance
Tim.deposit('400')
Tim.balance
Tim.withdraw(15)
Tim.balance
Tim.withdraw(200)
Tim.balance
Tim.withdraw(-20)
Tim.balance
Tim.withdraw('Five')
Tim.balance
Tim.withdraw(0)
Tim.balance

Tim.savings
Tim.transfer('cts', 5)
Tim.balance
Tim.savings
Tim.transfer('stc', 1)
Tim.balance
Tim.savings
Tim.transfer('stc', 5)
Tim.balance
Tim.savings
Tim.transfer('cts', -1)
Tim.balance
Tim.savings
Tim.transfer('stc', '2')
Tim.balance
Tim.savings
Tim.transfer('cts', '1')
Tim.balance
Tim.savings
Tim.transfer('cts', 0)
Tim.transfer('stc', 0)
Tim.balance
Tim.savings
Tim.transfer('dunno', 20)
