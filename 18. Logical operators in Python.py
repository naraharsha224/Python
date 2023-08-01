'''
Logical operators are used to combine conditional statements.

and: This operator returns True if both operands are true; otherwise, it returns False. If the first operand is False, the second operand is not evaluated because the result will always be False.

or: This operator returns True if at least one of the operands is true; otherwise, it returns False. If the first operand is True, the second operand is not evaluated because the result will always be True.

not: This operator returns the opposite boolean value of the operand. If the operand is True, not will return False, and if the operand is False, not will return True.
'''

# 'and' Examples:
x = 10
y = 20

# Both conditions are True, so the result is True.
result1 = (x > 5) and (y < 30)  # True

# The first condition is False, so the second condition is not evaluated,
# and the result is False.
result2 = (x > 15) and (y < 30)  # False


# 'or' Examples:
x = 10
y = 20

# At least one of the conditions is True, so the result is True.
result3 = (x > 15) or (y < 30)  # True

# Both conditions are False, so the result is False.
result4 = (x > 15) or (y < 10)  # False


# 'not' Examples:
x = True
y = False

# The opposite of True is False.
result5 = not x  # False

# The opposite of False is True.
result6 = not y  # True
