from abc import abstractmethod
from random import randint
from .Account import Account
from .Transaction import Transaction, TransactionType

class SavingsAccount(Account):
    MIN_DEPOSIT = 500
    
    def __init__(self):
        self.number = 12345
        self.balance = 0
        self.transactions = []

    def create(self, initialDeposit):
        if initialDeposit < self.MIN_DEPOSIT:
            print('Initial deposit insufficient')
        else:
            self.number = randint(10000, 99999)
            self.balance = initialDeposit
            self.transactions.append(Transaction(transaction_type = TransactionType.Deposit, amount = initialDeposit))
            print(f'Account created with initial deposit of: {initialDeposit}')
    
    def withdraw(self, amount):
        if self.balance < amount:
            print('Insufficient balance')
        else:
            self.balance -= amount
            self.transactions.append(Transaction(transaction_type = TransactionType.WithDrawal, amount = amount))
            print(f'Withdrawal of: {amount}')
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction(transaction_type = TransactionType.Deposit, amount = amount))
        print(f'Deposit: {amount}')
