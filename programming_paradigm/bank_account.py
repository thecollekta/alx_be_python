# bank_account.py

class BankAccount():
    def __init__ (self, initial_balance=0):
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        self.account_balance = +-amount # should add the specified amount to account_balance.

    def withdraw(self, amount):
        
# should deduct the amount from account_balance if funds are sufficient, returning True; otherwise, return False and do not alter the balance.
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False
            
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}") # should print the current balance in a user-friendly format.