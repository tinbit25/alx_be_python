# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

def main():
    """Main function to handle user input and perform conversions."""
    while True:  # Loop for continuous interaction
        try:
            temperature = input("Enter the temperature to convert (or type 'exit' to quit): ")
            if temperature.lower() == 'exit':
                print("Exiting the temperature conversion tool.")
                break  # Exit the loop if the user types 'exit'
                
            # Validate and convert the input to float
            temperature = float(temperature)
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'C':
                converted = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted:.2f}°F")
            elif unit == 'F':
                converted = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted:.2f}°C")
            else:
                raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError as e:
            print(f"Invalid temperature. Please enter a numeric value. Error: {e}")

if __name__ == "__main__":
    main()