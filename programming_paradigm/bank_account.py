import sys
from bank_account import BankAccount

def main():
    """
    Interact with the BankAccount class using command line arguments.
    Supported commands: deposit:<amount>, withdraw:<amount>, display
    """
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    try:
        command, *params = sys.argv[1].split(':')
        amount = float(params[0]) if params else None

        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command.")
    except ValueError as e:
        print(f"Error: {e}")
    except IndexError:
        print("Invalid command format. Use <command>:<amount> where appropriate.")

if __name__ == "__main__":
    main()
