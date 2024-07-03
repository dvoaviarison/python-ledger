from enum import Enum

class TransactionType(Enum):
    Deposit = 'Deposit'
    WithDrawal = 'Withdrawal'
    
class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
