'''
In Python, membership operators are used to test whether a specific element belongs to a collection (like a string, list, tuple, set, or dictionary). Python provides two membership operators:

in: Evaluates to True if the element is found in the collection.
not in: Evaluates to True if the element is not found in the collection.
'''

fruits = ["apple", "banana", "orange", "grape"]
print("banana" in fruits)  # Output: True
print("mango" in fruits)   # Output: False


colors = {"red", "blue", "green"}
print("yellow" not in colors)  # Output: True
print("red" not in colors)     # Output: False
