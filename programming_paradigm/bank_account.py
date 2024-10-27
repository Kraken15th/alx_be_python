class BankAccount:
   """ A class representing a bank account with deposit, withdraw, and balance display functionalities. """
   def __init__(self, initial_balance=0.0):
      self._balance = initial_balance
def deposit(self, amount):
   self._balance += amount
   def withdraw(self, amount):
      if amount <= self._balance:
         self._balance -= amount
         return True
      else:
         return False
      def display_balance(self):
         print(f"Current Balance: ${self._balance:.2f}")