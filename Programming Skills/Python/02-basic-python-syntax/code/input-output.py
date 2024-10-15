# 1. Output with print()

# Basic Usage
print("Hello, World!")  # Prints a string
print(10)                # Prints an integer
print(3.14)              # Prints a float

# Printing Multiple Items
name = "Alice"
age = 30
print("Name:", name, "Age:", age)  # Prints: Name: Alice Age: 30

# Customizing Output
print("Hello", "World", sep="-")  # Prints: Hello-World
print("Hello", end=", ")
print("World!")                   # Prints: Hello, World!

# 2. Input with input()
user_input = input("Enter your name: ")  # Prompts the user for input
print("Hello,", user_input)                # Displays a greeting

# 3. Type Conversion
age = input("Enter your age: ")             # User inputs age as a string
age = int(age)                               # Convert age to an integer
print("Next year, you will be", age + 1)    # Calculate and display next year's age

# 4. Formatted Output

# Using f-Strings
print(f"{name} is {age} years old.")  # Prints: Alice is 30 years old.

# Using format() Method
print("{} is {} years old.".format(name, age))  # Prints: Alice is 30 years old.
