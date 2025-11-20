def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def modulus(a,b):
    return a % b
def power(a,b):
    return a ** b
def floor_divide(a,b):
    if b == 0:
        return "Error: Division by zero"
    return a // b
def calculate(a, b, operation):
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide,
        'modulus': modulus,
        'power': power,
        'floor_divide': floor_divide
    }
    func = operations.get(operation)
    if func:
        return func(a, b)
    else:
        return "Error: Invalid operation"
if __name__ == "__main__":
    a = 10
    b = 5
    print("Addition:", calculate(a, b, 'add'))
    print("Subtraction:", calculate(a, b, 'subtract'))
    print("Multiplication:", calculate(a, b, 'multiply'))
    print("Division:", calculate(a, b, 'divide'))
    print("Modulus:", calculate(a, b, 'modulus'))
    print("Power:", calculate(a, b, 'power'))
    print("Floor Division:", calculate(a, b, 'floor_divide'))

# Example of invalid operation
    print("Invalid Operation:", calculate(a, b, 'invalid'))
    