import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Guessing Game!")
print("Geuss a number between 1 and 100?")

while True:
    guess = input("Enter your guess: ")
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break