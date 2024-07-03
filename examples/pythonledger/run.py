# Install the package before run: 
# `pip3 install .`

import os
from termcolor import colored
from pythonledger import SavingsAccount

user = os.getlogin()
initialDeposit = int(input(f'Hi {user}! Enter initial deposit: '))
account = SavingsAccount()
account.create(initialDeposit)
while True:
    print('==================================')
    print('Menu')
    print('==================================')
    print('1- Withdraw From Savings Account')
    print('2- Deposit To Savings Account')
    print('3- Show transactions')
    print('0- Exit')
    print('==================================')
    userChoice = int(input('Enter your choice: '))
    
    if userChoice == 1:
        amount = int(input(f'Hi {user}! Enter amount to withdraw: '))
        account.withdraw(amount)
        print(colored(f'Current balance is: {account.balance}', 'green'))
    if userChoice == 2:
        amount = int(input(f'Hi {user}! Enter amount to deposit: '))
        account.deposit(amount)
        print(colored(f'Current balance is: {account.balance}', 'green'))
    if userChoice == 3:
        print(colored(f'======= Transactions =========', 'red'))
        for transaction in account.transactions:
            print(f'{transaction.transaction_type.name} - {transaction.amount}')
        print(colored(f'==============================', 'red'))
    else:
        if userChoice == 0:
            quit()