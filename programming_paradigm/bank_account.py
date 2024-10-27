class BankAccount:
  """
  Represents a bank account with deposit, withdrawal, and balance display functionalities.
  """

  def __init__(self, initial_balance=0.0):
    """
    Initializes a BankAccount object with an optional starting balance (defaults to 0).
    """
    self.account_balance = initial_balance

  def deposit(self, amount):
    """
    Deposits the specified amount into the account and updates the balance.
    """
    self.account_balance += amount

  def withdraw(self, amount):
    """
    Attempts to withdraw the specified amount. Returns True on success, False on failure.
    """
    if amount <= self.account_balance:
      self.account_balance -= amount
      return True
    else:
      return False

  def display_balance(self):
    """
    Prints the current account balance in a user-friendly format.
    """
    print(f"Current Balance: ${self.account_balance:.2f}")  # Format balance with 2 decimal places
