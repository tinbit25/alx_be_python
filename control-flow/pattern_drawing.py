
def draw_square_pattern():
    try:
        size = int(input("Enter the size of the pattern: "))
 
        if size <= 0:
            print("Please enter a positive integer.")
            return
  
        for row in range(size):
            for col in range(size):
                print("*", end="") 
            print() 
    
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    draw_square_pattern()
