'''
In Python, a list is a built-in data structure that allows you to store a collection of elements in a specific order. 
Lists are mutable, which means you can modify, add, or remove elements after the list is created. 
Lists are defined using square brackets ([]) and can hold elements of different data types, including integers, floats, strings, or even other lists.
'''

# Shopping List:
# Imagine you are creating a shopping list. Here's how you can create a list of items and perform some common operations:
# Creating a shopping list
shopping_list = ["apples", "bananas", "milk", "bread"]

# Accessing elements
print(shopping_list[0])  # Output: "apples"

# Modifying elements
shopping_list[2] = "orange juice"
print(shopping_list)  # Output: ["apples", "bananas", "orange juice", "bread"]

# Adding elements
shopping_list.append("eggs")
print(shopping_list)  # Output: ["apples", "bananas", "orange juice", "bread", "eggs"]

# Removing elements
shopping_list.remove("bananas")
print(shopping_list)  # Output: ["apples", "orange juice", "bread", "eggs"]


##################################################################################
# To-Do List:
# Let's create a to-do list and manipulate its elements:

# Creating a to-do list
todo_list = ["workout", "study", "meeting", "read"]

# Checking if an item is in the list
print("study" in todo_list)  # Output: True

# Inserting elements
todo_list.insert(1, "lunch")
print(todo_list)  # Output: ["workout", "lunch", "study", "meeting", "read"]

# Removing elements by index
del todo_list[0]
print(todo_list)  # Output: ["lunch", "study", "meeting", "read"]


##################################################################################
# Temperature Data:
# Suppose you want to keep track of temperature data for different cities:

# Creating a list of temperature data
temperature_data = [25.5, 30.2, 22.8, 28.7, 24.9]

# Getting the number of elements
num_temperatures = len(temperature_data)
print(num_temperatures)  # Output: 5

# Finding the maximum temperature
max_temp = max(temperature_data)
print(max_temp)  # Output: 30.2

# Sorting the temperatures
temperature_data.sort()
print(temperature_data)  # Output: [22.8, 24.9, 25.5, 28.7, 30.2]

################################################################################
# Nested Lists:
# Lists can contain other lists, allowing you to represent more complex data structures:

# Creating a nested list (matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in the matrix
print(matrix[1][2])  # Output: 6

# Adding a new row to the matrix
new_row = [10, 11, 12]
matrix.append(new_row)
print(matrix)
# Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
















