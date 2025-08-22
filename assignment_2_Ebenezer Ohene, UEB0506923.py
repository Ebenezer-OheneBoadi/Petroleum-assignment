# ASSIGNMENT 2 PET ENG 200

import string
import math

# Task 1
def to_lowercase(s):
    return s.lower()

# Task 2
def swap_case(s):
    return s.swapcase()

# Task 3
def remove_uppercase(s):
    return ''.join(ch for ch in s if not ch.isupper())

# Task 4
def count_case(s):
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    return f"Uppercase: {upper}, Lowercase: {lower}"

# Task 5
def remove_non_letters(s):
    return ''.join(ch for ch in s if ch.isalpha())

# Task 6
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Task 7
def format_names(names):
    print("Name Table:")
    for name in names:
        print(name.center(20, ' '))

# Task 8
def clean_string(s):
    s = s.strip()
    s = ''.join(ch for ch in s if ch not in string.punctuation)
    s = s.replace(" ", "")
    return s


# ------------------ TESTING ------------------
if __name__ == "__main__":
    # Task 1
    print("Task 1:", to_lowercase("Hello"))
    
    # Task 2
    print("Task 2:", swap_case("HeLLo WoRLd"))

    # Task 3
    print("Task 3:", remove_uppercase("HelloWorld"))

    # Task 4
    print("Task 4:", count_case("EngiNEEr"))

    # Task 5
    print("Task 5:", remove_non_letters("Data-Driven@2025!"))

    # Task 6
    print("Task 6:", triangle_area(3, 4, 5))

    # Task 7
    print("\nTask 7:")
    format_names(["Alice", "Bob", "Charlotte", "David"])

    # Task 8
    print("\nTask 8:", clean_string("   Hello, World!    "))
