# match_case_calculator

# Prompt user for input
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

# Ask user to choose operation
operation = input('Choose the operation (+, -, *, /): ')

# Perform calculation using Match Case 
match operation:
        case '+':
                result = num1 + num2
                print(f'The result is {result}.')
        case '-':
                result = num1 - num2
                print(f'The result is {result}.')
        case '*':
                result = num1 * num2
                print(f'The result is {result}.')
        case '/':
                if num2 != 0:
                    result = num1 / num2
                    print(f'The result is {result}.')
                else:
                    print("cannot divide by zero.")
        case _: print("Invalid operation")