"""
Python Variables
1.	Variables are like containers for storing data values.
2.	Variables names are case-sensitive
3.	Python has no command for declaring a variable. Variable will get create the moment you assign value to it.
4.	Variables can change type after they have been set.
5.	We can get the type variable using type() function.
"""

age=28
name='Harsha'
print(type(age))  # 
print(type(name))  # 

# Output:
#  <class 'int'>
#  <class 'str'>


# Variables can change type after they have been set.

a=28
a='Harsha'
print(type(a))

# Output:
#  <class 'str'>


"""
Variable Names
1.	A variable name must start with a letter or the underscore character.
2.	A variable name cannot start with a number.
3.	A variable name can only contain alpha-numeric and underscore.
4.	Variable names are case-sensitive (age, Age and AGE are three different variables)
"""
# Examples as below

_firstname='Harsha'  # Valid
first_name='Harsha'  # Valid
firstname_='Harsha'  # Valid
first1name='Harsha'  # Valid
1first_name='Harsha' # inValid
./firstname='Harsha' # invalid
first.name='Harsha'   # invalid


"""
Assign multiple values to variables
1.	Assign multiple values to multiple variables.
"""
a,b,c='apple','ball','cat'
print(a)
print(b)
print(c)

# Output
# apple
# ball
# cat

"""
2. 2.	One value to a multiple variable
"""

a=b=c=20
print(a)
print(b)
print(c)

# output

# 20
# 20
# 20

