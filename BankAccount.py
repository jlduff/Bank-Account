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