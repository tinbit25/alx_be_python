# Define Global Conversion Factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Get user input for temperature
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Convert based on the unit
        if unit == 'F':
            print(f"{temperature}°F is {convert_to_celsius(temperature):.2f}°C")
        elif unit == 'C':
            print(f"{temperature}°C is {convert_to_fahrenheit(temperature):.2f}°F")
        else:
            raise ValueError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
