# Ebens Calculator

name = input("Hello! What is your name? ")

print(f"Welcome to the simple calculator, {name}!")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = input("Enter 1, 2, 3, or 4: ")

if operation == "1":
    result = num1 + num2
    op_symbol = "+"
elif operation == "2":
    result = num1 - num2
    op_symbol = "-"
elif operation == "3":
    result = num1 * num2
    op_symbol = "*"
elif operation == "4":
    if num2 != 0:
        result = num1 / num2
        op_symbol = "/"
    else:
        print("Error: Division by zero is not allowed.")
        exit()
else:
    print("Invalid operation selected.")
    exit()

print(f"{num1} {op_symbol} {num2} = {result}")