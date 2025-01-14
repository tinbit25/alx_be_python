def display_menu():
    """Display the shopping list menu."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty list

    while True:
        display_menu()  # Call the menu before user input
        choice = input("Enter your choice: ")

        # Ensure choice is numeric and valid
        if choice.isdigit():
            choice = int(choice)
        else:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:  # Add item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the list.")

        elif choice == 2:  # Remove item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' not found in the list.")

        elif choice == 3:  # View list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == 4:  # Exit
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
