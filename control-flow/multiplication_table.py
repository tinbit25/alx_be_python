
def generate_multiplication_table():
    try:
      
        number = int(input("Enter a number to see its multiplication table: "))
       
        print(f"\nMultiplication Table for {number}:")
        for i in range(1, 11):
            result = number * i
            print(f"{number} * {i} = {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    generate_multiplication_table()
