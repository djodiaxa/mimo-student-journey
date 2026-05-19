"""
Simple Calculator - First Project
A basic calculator to practice Python fundamentals.
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def calculator():
    """Main calculator function"""
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit\n")
    
    while True:
        operation = input("Choose operation (+, -, *, /) or 'quit': ").strip()
        
        if operation.lower() == 'quit':
            print("Thanks for using the calculator!")
            break
        
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Try again.\n")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            result = None
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            
            if result is not None:
                print(f"Result: {result}\n")
        
        except ValueError:
            print("Invalid input. Please enter numbers only.\n")

if __name__ == "__main__":
    calculator()
