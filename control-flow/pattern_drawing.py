# pattern_drawing.py

# Prompt user for input
size = int(input('Enter the size of the pattern: '))

row = 0

# Use while loop to iterate each row
while row < size:
    # Use a for loop to print asteriks in row
    for _ in range(size):
        print("*", end="")
    # Print a newline character to move to next row
    print()
    # Move to the next row
    row += 1