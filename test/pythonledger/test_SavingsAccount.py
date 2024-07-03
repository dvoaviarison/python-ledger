import unittest
from pythonledger import SavingsAccount

class TestSavingsAccount(unittest.TestCase):
    def setUp(self):
        self.account = SavingsAccount()
        self.account.create(1000)
        
    def test_withdraw_sufficient_fund(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.balance, 700, 'Balance is incorrect')
        self.assertEqual(len(self.account.transactions), 2, 'Ledger corrupted')
        
    def test_withdraw_insufficient_fund(self):
        self.account.withdraw(1200)
        self.assertEqual(self.account.balance, 1000, 'Balance is incorrect')
        self.assertEqual(len(self.account.transactions), 1, 'Ledger corrupted')
        
    def test_deposit(self):
        self.account.deposit(300)
        self.assertEqual(self.account.balance, 1300, 'Balance is incorrect')
        self.assertEqual(len(self.account.transactions), 2, 'Ledger corrupted')