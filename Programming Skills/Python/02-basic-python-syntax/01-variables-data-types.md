### Variables and Data Types in Python

In Python, variables are used to store data values. A variable is essentially a name that refers to a value in memory, allowing you to manipulate that value later in your program. Python is dynamically typed, meaning you don’t need to declare a variable’s type explicitly; it is determined at runtime.

#### 1. Variables

**Creating Variables:**

- To create a variable, simply assign a value to a name using the equals sign (`=`).
- Variable names must start with a letter or an underscore, followed by letters, digits, or underscores.

**Example:**

```python
name = "Alice"  # String variable
age = 30        # Integer variable
height = 5.7    # Float variable
is_student = True  # Boolean variable
```

**Variable Naming Rules:**

- Must start with a letter (a-z, A-Z) or underscore (_).
- Can contain letters, digits (0-9), or underscores.
- Case-sensitive (e.g., `myVar` and `myvar` are different).
- Cannot be a reserved keyword (like `if`, `for`, `while`, etc.).

#### 2. Data Types

Python has several built-in data types that can be categorized into several main groups:

**1. Numeric Types:**

- **Integers (`int`)**: Whole numbers, e.g., `10`, `-5`.
- **Floats (`float`)**: Decimal numbers, e.g., `10.5`, `-3.14`.
- **Complex Numbers (`complex`)**: Numbers with a real and imaginary part, e.g., `2 + 3j`.

   **Example:**

```python
   a = 10        # int
   b = 3.14      # float
   c = 1 + 2j    # complex
```

**2. Sequence Types:**

- **Strings (`str`)**: Textual data enclosed in single or double quotes, e.g., `"Hello"` or `'World'`.
- **Lists (`list`)**: Ordered, mutable collections of items, e.g., `[1, 2, 3]` or `['a', 'b', 'c']`.
- **Tuples (`tuple`)**: Ordered, immutable collections of items, e.g., `(1, 2, 3)` or `('a', 'b', 'c')`.

   **Example:**

```python
   greeting = "Hello, World!"  # str
   numbers = [1, 2, 3, 4, 5]    # list
   coordinates = (10, 20)        # tuple
```

**3. Mapping Type:**

- **Dictionaries (`dict`)**: Unordered collections of key-value pairs, e.g., `{"name": "Alice", "age": 30}`.

   **Example:**

```python
   person = {"name": "Alice", "age": 30, "height": 5.7}  # dict
```

**4. Set Types:**

- **Sets (`set`)**: Unordered collections of unique items, e.g., `{1, 2, 3}`.

   **Example:**

```python
   unique_numbers = {1, 2, 3, 3}  # set
```

**5. Boolean Type:**

- **Booleans (`bool`)**: Represents `True` or `False`.

   **Example:**

```python
   is_active = True   # bool
   is_passed = False   # bool
```

#### 3. Type Checking

You can check the data type of a variable using the `type()` function:

```python
x = 10
print(type(x))  # <class 'int'>

y = 3.14
print(type(y))  # <class 'float'>

z = "Hello"
print(type(z))  # <class 'str'>
```

#### 4. Type Conversion

You can convert between different data types using built-in functions:

- **Convert to `int`**:

  ```python
  x = int(3.14)  # x will be 3
  ```
- **Convert to `float`**:

  ```python
  y = float(10)  # y will be 10.0
  ```
- **Convert to `str`**:

  ```python
  z = str(100)   # z will be "100"
  ```
- **Convert to `list`**:

  ```python
  a = list((1, 2, 3))  # a will be [1, 2, 3]
  ```

#### Summary

Understanding variables and data types is fundamental in Python programming. This knowledge allows you to store, manipulate, and work with different types of data efficiently in your applications. By practicing with various data types and variables, you can build a strong foundation for your Python programming skills.
