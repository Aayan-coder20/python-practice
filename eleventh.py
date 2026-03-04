
from eleventhfunc import add, subtract, multiply, divide

print("--- Calculator ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operation (+, -, *, /): ")

if operator == '+':
    result = add(num1, num2)

elif operator == '-':
    result = subtract(num1, num2)

elif operator == '*':
    result = multiply(num1, num2)

elif operator == '/':
    if num2 == 0:
        print(f"{num1} / {num2} = Not Defined")
        exit()
    result = divide(num1, num2)

else:
    print("Invalid operation")
    exit()

print(f"{num1} {operator} {num2} = {result}")



