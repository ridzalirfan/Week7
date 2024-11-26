import math

# Functions for arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Functions for trigonometric operations (in radians)
def cosine(x):
    return math.cos(x)

def sine(x):
    return math.sin(x)

def tangent(x):
    if math.cos(x) == 0:
        return "Error! Undefined (cosine is 0)"
    return math.tan(x)

def scientific_calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Cosine")
    print("6. Sine")
    print("7. Tangent")

    while True:
        try:
            choice = input("Enter choice (1/2/3/4/5/6/7): ")

            if choice in ('1', '2', '3', '4'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")

            elif choice in ('5', '6', '7'):
                angle = float(input("Enter angle in radians: "))

                if choice == '5':
                    print(f"cos({angle}) = {cosine(angle)}")
                elif choice == '6':
                    print(f"sin({angle}) = {sine(angle)}")
                elif choice == '7':
                    print(f"tan({angle}) = {tangent(angle)}")

            # Check if user wants to continue
            next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if next_calculation != 'yes':
                break
        except ValueError:
            print("Invalid input! Please enter numerical values.")
            
if __name__ == "__main__":
    scientific_calculator()
