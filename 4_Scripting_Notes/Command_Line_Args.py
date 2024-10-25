# Command Line Arguments calculator

import sys

# Check for the correct number of arguments
if len(sys.argv) != 4:
    print("Usage: python calculator.py <number1> <operator> <number2>")
    sys.exit(1)

# Get the command-line arguments
num1 = float(sys.argv[1])
operator = sys.argv[2]
num2 = float(sys.argv[3])

# Perform the operation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero")
        sys.exit(1)
else:
    print("Error: Unsupported operator. Use +, -, *, or /.")
    sys.exit(1)

# Display the result
print(f"Result: {result}")