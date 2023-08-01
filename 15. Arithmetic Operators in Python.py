'''
Arithmetic operators are used with numeric values to perform mathematical operations.


Addition (+): Adds two operands together.
Subtraction (-): Subtracts the right operand from the left operand.
Multiplication (*): Multiplies two operands.
Division (/): Divides the left operand by the right operand. The result is always a float, even if both operands are integers.
Floor Division (//): Performs integer division, discarding the decimal part of the result.
Modulus (%): Returns the remainder of the division between the left operand and the right operand.
Exponentiation (**): Raises the left operand to the power of the right operand.
'''

a = 10
b = 3

# Addition
result_add = a + b
print("Addition:", result_add)  # Output: 13

# Subtraction
result_sub = a - b
print("Subtraction:", result_sub)  # Output: 7

# Multiplication
result_mul = a * b
print("Multiplication:", result_mul)  # Output: 30

# Division
result_div = a / b
print("Division:", result_div)  # Output: 3.3333333333333335 (float result)

# Floor Division
result_floor_div = a // b
print("Floor Division:", result_floor_div)  # Output: 3 (integer result)

# Modulus
result_mod = a % b
print("Modulus:", result_mod)  # Output: 1

# Exponentiation
result_exp = a ** b
print("Exponentiation:", result_exp)  # Output: 1000
