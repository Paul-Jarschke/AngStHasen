bank_dict= {}
first_question=0

list_names=("Jan", "Paul", "Leon", "Laura")
values=(0,0,0,0)

def dictionary(list):
    for name in list_names:
        bank_dict[name]=0

dictionary(list_names)

# With lambda function

dictionary_lambda= map(lambda k,v:bank_dict.update({k:v}), list_names,values)
print(bank_dict)

# 2. Add to dictionary
# bank_dict[name]=value
# Remove:
# bank_dict.pop("name")

# Deposit money
def deposit(name):
    try:
        value= int(input("What amount would you like to add?"))
    except ValueError:
        print("please enter a number larger than 0")
    if (value)>=0:
        bank_dict[name]=bank_dict[name]+value
    else:
        print("please enter a number larger than 0")


def withdraw(name):
    try:
        value=int(input("please enter a number:"))
    except ValueError:
        print("please enter a number larger than 0")
    if (value)>=0:
        before = bank_dict[name]
        bank_dict[name]=bank_dict[name]-value
    else:
        print("please enter a number larger than 0")
    if(bank_dict[name]<0):
        bank_dict[name]=before
        print("Account is overdrawn")

# For example
deposit("Jan")
withdraw("Jan")
print(bank_dict)

