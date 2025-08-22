# ASSIGNMENT

# Task 1 – Variable Types
integer_value = 25
float_value = 10.5
welcome_message = "Welcome"S
valid_flag = True

print(type(integer_value), integer_value)
print(type(float_value), float_value)
print(type(welcome_message), welcome_message)
print(type(valid_flag), valid_flag)

# Task 2
converted_int = int(19.99)
print(converted_int, type(converted_int))

converted_str = str(50)
print(converted_str, type(converted_str))

converted_float = float("50")
print(converted_float, type(converted_float))

# Task 3 – Greeting Message
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello,", first_name, last_name)

# Task 4 – Fixing Type Error
years = 20
print("You are " + str(years) + " years old.")

# Task 5 – Repeat Word
word = input("What is your favourite word? ")
count = int(input("How many times should it be repeated? "))
print((word + " ") * count)
print(f"Your favourite word is {word} and it was repeated {count} times.")

# Task 6 – Match the Error
# a. print("Hello       → SyntaxError (missing closing quote)
# b. int("abc")        → ValueError (cannot convert string to int)
# c. "age" + 10        → TypeError (string and int cannot be added)