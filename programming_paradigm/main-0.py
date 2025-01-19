import sys
from bank_account import BankAccount

def main():
    # Initialize the bank account with a starting balance
    account = BankAccount(100)

    # Check for valid command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and amount
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Perform the requested command
    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        except ValueError as e:
            print(e)
    elif command == "withdraw" and amount is not None:
        try:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        except ValueError as e:
            print(e)
    elif command == "display":
        print(account.display_balance())
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
