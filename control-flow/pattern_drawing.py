# pattern_drawing.py

def draw_square_pattern():
    try:
        # Prompt the user for the pattern size
        size = int(input("Enter the size of the pattern: "))
        
        # Ensure the size is positive
        if size <= 0:
            print("Please enter a positive integer.")
            return
        
        # Outer for loop for rows
        for row in range(size):
            # Inner for loop for columns
            for col in range(size):
                print("*", end="")  # Print an asterisk without a newline
            print()  # Print a newline after each row
    
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

# Run the function
if __name__ == "__main__":
    draw_square_pattern()
