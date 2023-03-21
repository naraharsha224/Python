'''
Local Variables:
1.	Local variables are created inside a function.
2.	Local variables can be used inside a function only.
3.	Local variable is a variable that is defined within a function or block of code and is only accessible within that function or block. Local variables are not visible outside of the function or block in which they are defined, and they are destroyed once the function or block of code has completed execution.
4.	To define a local variable in Python, you simply assign a value to a variable name within a function or block of code. 
'''

# Here's an example:
def my_function():
    x = 5
    print(x)

my_function() # Output: 5

# In the above example, x is a local variable defined within the my_function() function. It is only accessible within that function and cannot be accessed outside of it.

# It's important to note that if you try to access a local variable outside of the function or block in which it is defined, you will get a NameError. For example:


def my_function():
    x = 5

my_function()
print(x) # NameError: name 'x' is not defined

# In the above example, trying to access the x variable outside of the my_function() function results in a NameError, because x is a local variable that only exists within the function.


'''
Global Variables
1.	Global variables are created outside a function.
2.	Global variables can be used everywhere, both inside and outside a function.
3.	If we create a variable with same name inside a function, still both local and global variable are different. Local variables can be used only within the function or a code of block.

'''

y='Vardhan' # Here Y is a Global variable
def myfun():
    y = 'Harsha' # Here x is a local vairable
    print(y) # It'll take y as Harsha only(Local)

myfun()
print(y) # It'll take Y as Vardhan (Global)


'''
Global Keyword
1. In Python, the global keyword is used to indicate that a variable is a global variable, rather than a local variable within a function or block of code.
2. When a variable is defined within a function or block of code, it is by default a local variable, meaning it can only be accessed within that function or block of code. 
3. However, if you want to modify a global variable from within a function or block of code, you need to use the global keyword to indicate that you want to use the global variable, rather than create a new local variable with the same name.
'''
# Here's an example:

x = 5
def my_function():
    global x
    x = 10

my_function()
print(x) # Output: 10

# In the above example, the global keyword is used to indicate that we want to use the global variable x, rather than create a new local variable with the same name. 
# The value of x is then modified within the my_function() function, and when we print the value of x outside of the function, it has been updated to 10.
