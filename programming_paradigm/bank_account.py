class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance."""
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount > 0:
            self._account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a positive amount from the account.
        Returns True if successful, False if insufficient funds.
        """
        if amount > 0:
            if self._account_balance >= amount:
                self._account_balance -= amount
                return True
            else:
                return False
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def display_balance(self):
        """Return the current balance in a formatted string."""
        return f"Current Balance: ${self._account_balance:.2f}"
