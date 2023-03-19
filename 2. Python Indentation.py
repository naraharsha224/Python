# Python Indentation:
# 1.	Indentation means spaces at the beginning of the code line.
# 2.	Used to define the scope and hierarchy of the code blocks.
# 3.	Python doesn’t use any curly brace or any special characters, instead it uses whitespace indentation.
# 4.	Python code blocks start with colon(:).
# 5.	The indentation level must be same throughout the code block.
# 6.	Python will throw error if we skip the indentation. Number of spaces is upto the programmer. But there should be atleast one.


# Example 1

if x > 0:
    print("x is positive")
else:
    print("x is not positive")


# Here, the if statement and the else statement are separate code blocks, each with their own level of indentation. 
# The statements within the if and else blocks are indented to the right to indicate that they are part of the respective code blocks.


# Example 2

if x > 5:
    print("x is greater than 5")
    if x > 10:
        print("x is also greater than 10")
print("This statement is not part of the if block")

# In this example, the code block for the outer if statement starts with the colon (:) and is indented to the right. 
# The code block for the nested if statement is further indented to the right. 
#The statement outside of the if block is not indented and is at the same level of indentation as the outer if statement.


# Example 3

for i in range(5):
    print(i)
    if i == 2:
        print("The value of i is 2")
print("The loop has ended")

# In this example, the code block for the for loop starts with the colon (:) and is indented to the right. 
# The code block for the if statement is further indented to the right. 
# The print statement outside of the if block is not indented and is at the same level of indentation as the for loop.


# Example 4

while True:
    answer = input("Do you want to continue? (y/n) ")
    if answer == "n":
        break
    print("Continuing...")
print("Done!")

# In this example, the code block for the while loop starts with the colon (:) and is indented to the right. 
# The code block for the if statement is further indented to the right. 
# The print statement outside of the while loop is not indented and is at the same level of indentation.
