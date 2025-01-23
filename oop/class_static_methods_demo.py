class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers, printing the calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Uncomment to test within this file
if __name__ == "__main__":
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")
   
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")