# 1. Creating Lists

# An empty list
empty_list = []

# A list of integers
numbers = [1, 2, 3, 4, 5]

# A list of mixed data types
mixed_list = [1, "Hello", 3.14, True]

# 2. Accessing Elements

# Accessing elements
first_number = numbers[0]  # 1
second_number = numbers[1]  # 2
last_number = numbers[-1]    # 5
last_number = numbers[-2]    # 4

# 3. Modifying Lists

# Changing an element
numbers[0] = 10  # List becomes [10, 2, 3, 4, 5]

# Adding elements
numbers.append(6)  # List becomes [10, 2, 3, 4, 5, 6]

# Inserting elements at a specific index
numbers.insert(1, 15)  # List becomes [10, 15, 2, 3, 4, 5, 6]

# Removing elements
numbers.remove(15)  # List becomes [10, 2, 3, 4, 5, 6]

# Popping an element (removes and returns the last item)
last_item = numbers.pop()  # last_item = 6, List becomes [10, 2, 3, 4, 5]

# 4. List Operations

# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2  # [1, 2, 3, 4, 5, 6]

# Repetition
repeated_list = [0] * 4  # [0, 0, 0, 0]

# Slicing
sub_list = numbers[1:4]  # Get elements from index 1 to 3 (2, 3, 4)

# 5. List Functions and Methods

# Finding the length of a list
length = len(numbers)  # 5

# Sorting a list
numbers.sort()  # Sorts the list in ascending order

# Reversing a list
numbers.reverse()  # Reverses the order of the list

# 6. Nested Lists

# A nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in a nested list
element = matrix[1][2]  # 6 (2nd list, 3rd element)
