'''

In Python, a "set" is a built-in data structure that represents an unordered collection of unique elements. 
This means that a set can only contain distinct values, and it does not allow duplicate elements. 
Sets are useful for tasks such as removing duplicates from a list, performing set operations like intersection and union, and checking membership of elements in constant time.

'''

# Unique Elements in a List:
# Sets are often used to find unique elements in a list. For example:

numbers = [1, 2, 3, 4, 3, 2, 5]
unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

############################################################################
# Membership Testing:
# You can efficiently check if an element is present in a set using the in operator:

fruits = {"apple", "banana", "orange", "grape"}
print("apple" in fruits)  # Output: True
print("pear" in fruits)   # Output: False

############################################################################
# Set Operations:
# Sets support various set operations like union, intersection, and difference:

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union_set = A.union(B)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}

intersection_set = A.intersection(B)
print(intersection_set)  # Output: {3, 4}

difference_set = A.difference(B)
print(difference_set)  # Output: {1, 2}

############################################################################

# Creating a set
workshop_attendees = {"Alice", "Bob", "Charlie", "Alice", "David"}

# Duplicates are automatically removed
print(workshop_attendees)  # Output: {'Charlie', 'Bob', 'David', 'Alice'}

# Adding elements to a set
workshop_attendees.add("Eve")
print(workshop_attendees)  # Output: {'Charlie', 'Bob', 'David', 'Eve', 'Alice'}

# Removing an element from a set
workshop_attendees.remove("Bob")
print(workshop_attendees)  # Output: {'Charlie', 'David', 'Eve', 'Alice'}

# Checking membership
print("Alice" in workshop_attendees)  # Output: True
print("Bob" in workshop_attendees)    # Output: False

# Set operations
other_attendees = {"Frank", "Alice", "Eve"}

# Union
all_attendees = workshop_attendees.union(other_attendees)
print(all_attendees)  # Output: {'Charlie', 'Eve', 'David', 'Alice', 'Frank'}

# Intersection
common_attendees = workshop_attendees.intersection(other_attendees)
print(common_attendees)  # Output: {'Alice', 'Eve'}

# Difference
unique_to_workshop = workshop_attendees.difference(other_attendees)
print(unique_to_workshop)  # Output: {'Charlie', 'David'}

###############################################################################
