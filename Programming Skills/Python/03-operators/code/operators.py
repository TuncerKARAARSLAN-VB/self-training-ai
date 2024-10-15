# 1. Arithmetic Operators

# Example variables: initializing two numeric variables for arithmetic operations
a = 10  # First operand
b = 5   # Second operand

# Performing arithmetic operations and storing results in new variables
addition = a + b          # Adds a and b; result is 15
subtraction = a - b       # Subtracts b from a; result is 5
multiplication = a * b    # Multiplies a and b; result is 50
division = a / b          # Divides a by b; result is 2.0 (float)
floor_division = a // b   # Performs floor division of a by b; result is 2 (integer)
modulus = a % b           # Computes the remainder of a divided by b; result is 0
exponentiation = a ** b   # Raises a to the power of b; result is 100000 (10^5)

# 2. Comparison Operators

# Comparing values and storing Boolean results in new variables
is_equal = (a == b)              # Checks if a is equal to b; result is False
is_not_equal = (a != b)          # Checks if a is not equal to b; result is True
is_greater = (a > b)             # Checks if a is greater than b; result is True
is_less = (a < b)                # Checks if a is less than b; result is False
is_greater_equal = (a >= b)      # Checks if a is greater than or equal to b; result is True
is_less_equal = (a <= b)         # Checks if a is less than or equal to b; result is False

# 3. Logical Operators

# Using logical operators to evaluate conditions and store results
logical_and = (a > 0) and (b > 0)  # Evaluates to True if both conditions are True (a > 0 and b > 0)
logical_or = (a > 0) or (b < 0)    # Evaluates to True if at least one condition is True (a > 0 or b < 0)
logical_not = not (a > 0)          # Reverses the Boolean value; True if a is not greater than 0

# 4. Assignment Operators

# Example variable: initializing a variable c with the value of a
c = a  # Simple assignment; c now holds the value of a (10)

# Performing compound assignment operations
c += b   # Adds b to c; equivalent to c = c + b (10 + 5), c now is 15
c -= b   # Subtracts b from c; equivalent to c = c - b (15 - 5), c now is 10
c *= b   # Multiplies c by b; equivalent to c = c * b (10 * 5), c now is 50
c /= b   # Divides c by b; equivalent to c = c / b (50 / 5), c now is 10.0 (float)
c //= b  # Performs floor division on c by b; equivalent to c = c // b (10 // 5), c now is 2
c %= b   # Computes the remainder of c divided by b; equivalent to c = c % b (2 % 5), c now is 2
c **= b  # Raises c to the power of b; equivalent to c = c ** b (2 ** 5), c now is 32
