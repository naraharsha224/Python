'''
In Python, a tuple is an ordered, immutable collection of elements. Tuples are similar to lists, but unlike lists, once a tuple is created, its elements cannot be modified, added, or removed. 
Tuples are defined using parentheses () and can contain elements of different data types. Since tuples are immutable, they are typically used to store a fixed set of related items.
'''

##########################################################
# Coordinates: Tuples are commonly used to store coordinates in a 2D space, such as (x, y) points.
# Example of a 2D coordinate tuple
coordinate = (10, 5)

# Accessing elements of the tuple
x, y = coordinate
print("x:", x)  # Output: x: 10
print("y:", y)  # Output: y: 5

###########################################################
# Student Information: Tuples can be used to store related information about a student.
# Example of a student information tuple
student_info = ("John Doe", 25, "Computer Science")

# Accessing elements of the tuple
name, age, major = student_info
print("Name:", name)    # Output: Name: John Doe
print("Age:", age)      # Output: Age: 25
print("Major:", major)  # Output: Major: Computer Science

#########################################################
# Point of Interest (POI) Data: Tuples can be used to store information about Points of Interest in a map.
# Example of a Point of Interest (POI) tuple
poi = ("Eiffel Tower", (48.8584, 2.2945))

# Accessing elements of the tuple
poi_name, (latitude, longitude) = poi
print("Name:", poi_name)      # Output: Name: Eiffel Tower
print("Latitude:", latitude)  # Output: Latitude: 48.8584
print("Longitude:", longitude) # Output: Longitude: 2.2945

