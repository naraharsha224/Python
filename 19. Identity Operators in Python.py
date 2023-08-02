'''
In Python, identity operators are used to compare the memory addresses of two objects to check if they refer to the same object or not. These operators are denoted by "is" and "is not." 
They are useful when you want to check if two variables point to the same object in memory, rather than just having the same value.

Here's a brief explanation of the identity operators:

is: This operator returns True if two variables refer to the same object in memory, and False otherwise.

is not: This operator returns True if two variables do not refer to the same object in memory, and False if they do.

'''

# Example 1
x = [1, 2, 3]
y = x  # Both x and y point to the same list object in memory

print(x is y)      # True
print(x is not y)  # False

# Example 2
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)      # False (a and b are two different objects in memory)
print(a is not b)  # True

# Example 3
c = [1, 2, 3]
d = c[:]  # Create a copy of the list c

print(c is d)      # False (c and d are different objects in memory)
print(c is not d)  # True
