# 1. Variables

# Creating Variables
name = "Alice"  # String variable storing the name "Alice"
age = 30        # Integer variable storing the age as 30
height = 5.7    # Float variable storing height as 5.7
is_student = True  # Boolean variable indicating if the person is a student

# Variable Naming Rules
# 1. Must start with a letter (a-z, A-Z) or underscore (_).
# 2. Can contain letters, digits (0-9), or underscores.
# 3. Case-sensitive (e.g., myVar and myvar are different).
# 4. Cannot be a reserved keyword (like if, for, while, etc.).

# 2. Data Types

# Numeric Types
a = 10        # Integer type (int) variable storing the value 10
b = 3.14      # Float type variable storing the value 3.14
c = 1 + 2j    # Complex type variable storing a complex number (1 + 2j)

# Sequence Types
greeting = "Hello, World!"  # String type (str) variable containing text
numbers = [1, 2, 3, 4, 5]    # List type variable containing a collection of integers
coordinates = (10, 20)        # Tuple type variable containing ordered pairs of integers

# Mapping Type
person = {"name": "Alice", "age": 30, "height": 5.7}  # Dictionary type (dict) with key-value pairs

# Set Types
unique_numbers = {1, 2, 3, 3}  # Set type variable containing unique integers; duplicates are removed

# Boolean Type
is_active = True   # Boolean type variable indicating active status
is_passed = False   # Boolean type variable indicating pass/fail status

# 3. Type Checking
x = 10
print(type(x))  # Outputs: <class 'int'>, showing the data type of x

y = 3.14
print(type(y))  # Outputs: <class 'float'>, showing the data type of y

z = "Hello"
print(type(z))  # Outputs: <class 'str'>, showing the data type of z

# 4. Type Conversion
# Convert to int
x = int(3.14)  # Converts float 3.14 to integer 3 and assigns it to x

# Convert to float
y = float(10)  # Converts integer 10 to float 10.0 and assigns it to y

# Convert to str
z = str(100)   # Converts integer 100 to string "100" and assigns it to z

# Convert to list
a = list((1, 2, 3))  # Converts a tuple (1, 2, 3) to a list [1, 2, 3] and assigns it to a
