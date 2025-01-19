# Define Global Conversion Factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt user for temperature input
        temp_input = input("Enter a temperature value: ").strip()
        
        # Validate the temperature input
        if not temp_input.replace('.', '', 1).replace('-', '', 1).isdigit():
            raise ValueError("Invalid temperature value. Please enter a valid number.")
        
        temperature = float(temp_input)

        # Prompt user for unit
        unit = input("Enter the unit of temperature (C for Celsius, F for Fahrenheit): ").strip().upper()
        
        # Validate the unit input and perform the conversion
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature} in Fahrenheit is {converted_temp:.2f} Celsius.")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature} in Celsius is {converted_temp:.2f} Fahrenheit.")
        else:
            raise ValueError("Invalid unit of temperature. Please enter 'C' or 'F'.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
