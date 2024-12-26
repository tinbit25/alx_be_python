# match_case_calculator.py

def calculator():
    try:
        # Prompt for user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ").strip()

        # Perform calculation using match case
        match operation:
            case "+":
                result = num1 + num2
                print(f"The result is {result}")
            case "-":
                result = num1 - num2
                print(f"The result is {result}")
            case "*":
                result = num1 * num2
                print(f"The result is {result}")
            case "/":
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result is {result}")
                else:
                    print("Cannot divide by zero.")
            case _:
                print("Invalid operation. Please choose +, -, *, or /.")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Run the calculator
if __name__ == "__main__":
    calculator()
