# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Define the conversion functions
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# User interaction
def main():
    while True:
        try:
            temperature = input("Enter the temperature to convert: ")
            temperature = float(temperature)  # Convert to float to check for numeric value
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'C':
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temp}°F")
                break  # Exit the loop after successful conversion
            elif unit == 'F':
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temp}°C")
                break  # Exit the loop after successful conversion
            else:
                print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()