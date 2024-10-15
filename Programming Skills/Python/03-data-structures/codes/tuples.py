# 1. Creating Tuples
# Using parentheses
my_tuple = (1, 2, 3)

# Without parentheses (tuple packing)
my_tuple2 = 4, 5, 6

# Using the tuple() constructor
my_tuple3 = tuple([7, 8, 9])

# Creating an empty tuple
empty_tuple = ()

# Creating a single-element tuple
single_element_tuple = (10,)

# 2. Accessing Tuple Elements
print(my_tuple[0])        # Output: 1
print(my_tuple[1:3])     # Output: (2, 3)

# 3. Modifying Tuples
# Converting to a list, modifying, then back to a tuple
my_list = list(my_tuple)  # Convert to list
my_list[0] = 4            # Modify the list
my_tuple = tuple(my_list) # Convert back to tuple
print(my_tuple)           # Output: (4, 2, 3)

# 4. Tuple Operations
# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2  # Output: (1, 2, 3, 4)
print(result)

# Repetition
my_tuple = (1, 2)
result = my_tuple * 3      # Output: (1, 2, 1, 2, 1, 2)
print(result)

# Membership Test
print(2 in my_tuple)       # Output: True
print(4 in my_tuple)       # Output: False

# Length of the tuple
print(len(my_tuple))       # Output: 2

# 5. Packing and Unpacking Tuples
# Packing
packed_tuple = (1, 2, 3)

# Unpacking
a, b, c = packed_tuple
print(a, b, c)             # Output: 1 2 3

# 6. Returning Multiple Values from a Function
def return_tuple():
    return (1, 'two', 3.0)

result_tuple = return_tuple()
print(result_tuple)        # Output: (1, 'two', 3.0)
