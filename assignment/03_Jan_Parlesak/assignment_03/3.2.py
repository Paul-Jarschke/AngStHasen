class Customer:
    def __init__(self,name,balance):
        self.name= name
        self.balance=balance

    def valid(input):
        if (type(input)==int):
            return True
        else:
            return False

    def add_balance(self,add):
        if Customer.valid(add):
            self.balance= int(self.balance + add)
        else:
            print("Pls enter a number")

    def withdraw(self,withdraw):
        if Customer.valid(withdraw) and (self.balance-withdraw)>0:
            self.balance= int(self.balance - withdraw)
        else:
            print("Try again pls")


class SavingsCustomer(Customer):
    def __init__(self,name,balance,savings_balance):
        super().__init__(name,balance)
        self.savings_balance= savings_balance


    def transfer_to_savings(self,amount):
        if type(amount)== int:
            if self.balance>amount:
                self.savings_balance= int(self.savings_balance+amount)
                self.balance= int(self.balance-amount)
            else:
                print("Amount is wrong")
        else:
            print("please enter a valid number")

    def transfer_from_savings(self, amount):
        if type(amount) == int:
            if self.savings_balance>amount:
                self.balance= int(self.balance +amount)
                self.savings_balance= int(self.savings_balance - amount)
            else:
                print("Amount is wrong")
        else:
            print("please enter a valid number")

