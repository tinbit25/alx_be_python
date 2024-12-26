# multiplication_table.py

def generate_multiplication_table():
    try:
        # Prompt user for a number
        number = int(input("Enter a number to see its multiplication table: "))
        
        # Generate and print the multiplication table
        print(f"\nMultiplication Table for {number}:")
        for i in range(1, 11):
            result = number * i
            print(f"{number} * {i} = {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Run the function
if __name__ == "__main__":
    generate_multiplication_table()
