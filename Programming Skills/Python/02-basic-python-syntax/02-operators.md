### Operators in Python

Operators are special symbols in Python that perform operations on variables and values. They can be categorized into different types based on the kind of operation they perform. Here, we'll discuss four main categories of operators: Arithmetic, Comparison, Logical, and Assignment.

#### 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations. They include:

- **Addition (`+`)**: Adds two operands.
- **Subtraction (`-`)**: Subtracts the second operand from the first.
- **Multiplication (`*`)**: Multiplies two operands.
- **Division (`/`)**: Divides the first operand by the second, resulting in a float.
- **Floor Division (`//`)**: Divides the first operand by the second and returns the largest whole number (integer).
- **Modulus (`%`)**: Returns the remainder of the division of the first operand by the second.
- **Exponentiation (`**`)**: Raises the first operand to the power of the second.

**Example:**

```python
a = 10
b = 5

addition = a + b  # 15
subtraction = a - b  # 5
multiplication = a * b  # 50
division = a / b  # 2.0
floor_division = a // b  # 2
modulus = a % b  # 0
exponentiation = a ** b  # 100000
```

#### 2. Comparison Operators

Comparison operators are used to compare two values. They return a Boolean result: `True` or `False`. The common comparison operators are:

- **Equal to (`==`)**: Checks if two operands are equal.
- **Not equal to (`!=`)**: Checks if two operands are not equal.
- **Greater than (`>`)**: Checks if the first operand is greater than the second.
- **Less than (`<`)**: Checks if the first operand is less than the second.
- **Greater than or equal to (`>=`)**: Checks if the first operand is greater than or equal to the second.
- **Less than or equal to (`<=`)**: Checks if the first operand is less than or equal to the second.

**Example:**

```python
is_equal = (a == b)  # False
is_not_equal = (a != b)  # True
is_greater = (a > b)  # True
is_less = (a < b)  # False
is_greater_equal = (a >= b)  # True
is_less_equal = (a <= b)  # False
```

#### 3. Logical Operators

Logical operators are used to combine conditional statements. They evaluate to `True` or `False`. The main logical operators are:

- **Logical AND (`and`)**: Returns `True` if both operands are true.
- **Logical OR (`or`)**: Returns `True` if at least one of the operands is true.
- **Logical NOT (`not`)**: Reverses the Boolean value of the operand.

**Example:**

```python
logical_and = (a > 0) and (b > 0)  # True
logical_or = (a > 0) or (b < 0)  # True
logical_not = not (a > 0)  # False
```

#### 4. Assignment Operators

Assignment operators are used to assign values to variables. The most basic assignment operator is the equals sign (`=`). However, there are several compound assignment operators that combine an arithmetic operation with assignment:

- **Simple assignment (`=`)**: Assigns the value of the right operand to the left operand.
- **Add and assign (`+=`)**: Adds the right operand to the left operand and assigns the result to the left operand.
- **Subtract and assign (`-=`)**: Subtracts the right operand from the left operand and assigns the result to the left operand.
- **Multiply and assign (`*=`)**: Multiplies the left operand by the right operand and assigns the result to the left operand.
- **Divide and assign (`/=`)**: Divides the left operand by the right operand and assigns the result to the left operand.
- **Floor divide and assign (`//=`)**: Performs floor division and assigns the result.
- **Modulus and assign (`%=`)**: Performs modulus and assigns the result.
- **Exponentiation and assign (`**=`)**: Performs exponentiation and assigns the result.

**Example:**

```python
c = a  # Simple assignment
c += b  # Equivalent to c = c + b
c -= b  # Equivalent to c = c - b
c *= b  # Equivalent to c = c * b
c /= b  # Equivalent to c = c / b
c //= b  # Equivalent to c = c // b
c %= b  # Equivalent to c = c % b
c **= b  # Equivalent to c = c ** b
```

### Summary

Understanding operators in Python is crucial for performing operations and making comparisons between values. They allow you to write dynamic and complex code efficiently. Familiarizing yourself with these operators will help you manipulate data effectively in your programs.

[All Codes](./code/operators.py)