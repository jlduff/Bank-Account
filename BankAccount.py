import random

class BankAccount():
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

def AccountNumRand():
    number = random.randint(10000000, 99999999)
    return number

init_balance = 0

def get_balance(self):
    return f'Your current balance is ${self.balance}. Would you like to do anything today?'

def withdraw(self, amount):
    if self.balance >= amount:
        
        self.balance -= amount
        print(f"You have withdrawn ${amount} from your account. Your balance is now ${self.balance}")
    else:
        self.balance -= 10
        self.balance -= amount

    return f"{self.full_name}, there are insufficient funds in your account. You will be charged an overdraft fee of $10. \n Your balance is now ${self.balance}"

def deposit(self, amount):
    self.balance += amount 
    return f'You have deposited ${amount} into your account \n Your balance is now ${self.balance}'

def print_receipt(self, full_name, account_number, routing_number, balance):
    return self.balance

def add_interest(self):
    interest = self.balance *  0.00083 
    return interest

routing_num = 203049495

def print_receipt(self, full_name, routing_number, account_number, balance):
    print(f"Name: {self.full_name}")
    print(f"Routing Number: {self.routing_number}") 
    print(f"Account Number: {self.account_number}")
    print(f"Balance: ${self.balance}")



