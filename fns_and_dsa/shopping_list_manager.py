# shopping_list_manager.py

def display_menu():
    """Display the menu options for the shopping list manager."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list
    while True:
        display_menu()  # Display the menu
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("Current Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is currently empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()