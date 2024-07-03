from abc import abstractmethod

class Account:    
    @abstractmethod
    def create(self, initialDeposit):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass
    
    @abstractmethod
    def deposit(self, amount):
        pass
