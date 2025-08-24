name = input("Hello! What is your name? ")

number_input = input(f"Good Day!, {name}! Please enter a number: ")

if number_input.isdigit():
    number = int(number_input)
    
    if number % 2 == 0:
        print(f"{name}, the number {number} is even.")
    else:
        print(f"{name}, the number {number} is odd.")
else:
    print("Not a valid number. Please try another number.")