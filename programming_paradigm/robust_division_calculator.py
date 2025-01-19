def safe_divide(numerator, denominator):
    """
    Perform division with robust error handling.

    Args:
        numerator: The numerator as a string or float.
        denominator: The denominator as a string or float.

    Returns:
        str: The result of the division or an appropriate error message.
    """
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform division
        result = numerator / denominator
        return f"The result of the division is {result:.2f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
