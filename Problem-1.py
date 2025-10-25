class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error: Division by zero not allowed!"
        return self.a / self.b
# Take inputs from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ").lower()

# Create object
calc = Calculator(a, b)

# Decide which operation to perform
if operation == "add":
    result = calc.add()
elif operation == "subtract":
    result = calc.subtract()
elif operation == "multiply":
    result = calc.multiply()
elif operation == "divide":
    result = calc.divide()
else:
    result = "Invalid operation type!"
print("Result:", result)

