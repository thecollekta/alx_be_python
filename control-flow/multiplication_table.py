# multiplication_table.py

# Prompt user for a number
number = int(input("Enter a number: "))

for count in range(1, 11):
    product = number * count
    print(number, "x", count, "=", product)