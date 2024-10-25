import logging

# Configure logging settings
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def calculate(num1, operator, num2):
    logging.info(f"Performing calculation: {num1} {operator} {num2}")
    
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
            logging.warning("Attempted division by zero.")
            return None
    else:
        logging.error(f"Unsupported operator: {operator}")
        return None

    logging.info(f"Result: {result}")
    return result

# Example usage
calculate(10, '+', 5)     # Expected to log info messages
calculate(10, '/', 0)     # Expected to log a warning
calculate(10, '$', 5)     # Expected to log an error