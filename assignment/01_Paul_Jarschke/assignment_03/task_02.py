# Task 2 - Classes

# The manager thinks that the simple bookkeeping system you have built is not powerful enough.
# She requests that you start from scratch and use classes instead.

# Write a simple class with appropriate constructor __init__ that initializes an object of class Customer tracking the
# same information as in Task 01.
# Write two simple methods for class Customer that allow you to deposit and withdraw money for a given customer object.
# Include error messages for not permissible inputs , e.g., withdrawing negative amounts or overdrawing the account.
# (Inheritance) Write a child class SavingsCustomer that inherits its features from the parent class Customer.
# A savings customer has an extra savings balance for receiving extra interest.
# The class should have a method to transfer money back and forth between the accounts' main balance as well as the
# savings balance. Do not forget to add reasonable error messages.

class Customer:
    """A simple attempt to model a customer"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, value):
        """Add money to checking account."""
        if type(value) != int and type(value) != float:
            print('You can only enter numerical values!')
        elif value < 0:
            print('You cannot deposit negative amounts!')
        else:
            self.balance += value

    def withdraw(self, value):
        """Remove money from checking account"""
        if type(value) != int and type(value) != float:
            print('You can only enter numerical values!')
        elif value < 0:
            print('You cannot withdraw negative amounts!')
        elif value > self.balance:
            print(f'{self.name} does not have enough money in his/her bank account! '
                  f'You can only withdraw up to {self.balance}$.')
        else:
            self.balance += -value


class SavingsCustomer(Customer):
    """A simple attempt to model a subclass of customer."""

    def __init__(self, name, balance, savings):
        # inherit all attributes from Customer
        super().__init__(name, balance)
        # add subclass-specific attribute
        self.savings = savings

    def transfer_to_checking(self, value):
        """Transfer money from savings to balance"""
        if type(value) != int and type(value) != float:
            print('You can only enter numerical values!')
        elif value < 0:
            print('You cannot transfer negative amounts!')
        elif value > self.savings:
            print(f'{self.name} does not have enough money in his/her savings account! '
                  f'You can only transfer up to {self.savings}$.')
        else:
            self.savings -= value
            self.balance += value

    def transfer_to_savings(self, value):
        """Transfer money from balance to savings"""
        if type(value) != int and type(value) != float:
            print('You can only enter numerical values!')
        elif value < 0:
            print('You cannot transfer negative amounts!')
        elif value > self.balance:
            print(f'{self.name} does not have enough money in his/her checking account! '
                  f'You can only transfer up to {self.balance}$.')
        else:
            self.balance -= value
            self.savings += value


# Testing
# just remove the "#" of the method you want to test
p = SavingsCustomer(name='Paul', balance=50, savings=1000)
print('Account after initiation')
print(f'Name: {p.name}  Balance: {p.balance}$  Savings: {p.savings}$\n')
print('Account after test')
# p.deposit('12')
# p.deposit(-100)
# p.deposit(50)

# p.withdraw('12')
# p.withdraw(-10)
# p.withdraw(1000000)
# p.withdraw(50)

# p.transfer_to_checking('12')
# p.transfer_to_checking(-12)
# p.transfer_to_checking(10000000)
# p.transfer_to_checking(500)

# p.transfer_to_savings('12')
# p.transfer_to_savings(-10)
# p.transfer_to_savings(100000000)
# p.transfer_to_savings(50)

print(f'Name: {p.name}  Balance: {p.balance}$  Savings: {p.savings}$\n')
