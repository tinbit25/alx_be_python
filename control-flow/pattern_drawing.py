def draw_square_pattern():
    try:
        size = int(input("Enter the size of the pattern: "))
        
        if size <= 0:
            print("Please enter a positive integer.")
            return
        
        row = 0
        while row < size:
            col = 0
            while col < size:
                print("*", end="")
                col += 1
            print()  
            row += 1
    
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    draw_square_pattern()
