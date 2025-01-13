def display_menu():
    """Display the shopping list menu."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to manage the shopping list."""
    shopping_list = []  # Start with an empty list

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':  # Add item
            item = input("Enter the item to add: ").strip()
            if item:  # Ensure the item is not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("Item cannot be empty. Please try again.")

        elif choice == '2':  # Remove item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the list.")

        elif choice == '3':  # View list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':  # Exit
            print("Goodbye!")
            break

        else:  # Handle invalid input
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
