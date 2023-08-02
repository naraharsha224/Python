'''
In Python, bitwise operators are used to perform operations on individual bits of integers. These operators allow you to manipulate the binary representation of integers directly. Python provides the following bitwise operators:

Bitwise AND (&): It performs a bitwise AND operation on two numbers. Each bit of the result is set to 1 only if both corresponding bits of the input operands are 1; otherwise, it is set to 0.

Bitwise OR (|): It performs a bitwise OR operation on two numbers. Each bit of the result is set to 1 if either of the corresponding bits of the input operands is 1.

Bitwise XOR (^): It performs a bitwise XOR (exclusive OR) operation on two numbers. Each bit of the result is set to 1 if the corresponding bits of the input operands differ; otherwise, it is set to 0.

Bitwise NOT (~): It performs a bitwise NOT operation on a single number. It flips all the bits, changing 1s to 0s and 0s to 1s.

Bitwise Left Shift (<<): It shifts the bits of a number to the left by the specified number of positions. It is equivalent to multiplying the number by 2 to the power of the shift amount.

Bitwise Right Shift (>>): It shifts the bits of a number to the right by the specified number of positions. It is equivalent to dividing the number by 2 to the power of the shift amount.
'''

# Sample integers for bitwise operations
a = 15    # Binary: 1111
b = 7     # Binary: 0111

# Bitwise AND
result_and = a & b
print("Bitwise AND:", result_and)  # Output: 7 (Binary: 0111)

# Bitwise OR
result_or = a | b
print("Bitwise OR:", result_or)    # Output: 15 (Binary: 1111)

# Bitwise XOR
result_xor = a ^ b
print("Bitwise XOR:", result_xor)  # Output: 8 (Binary: 1000)

# Bitwise NOT
result_not_a = ~a
result_not_b = ~b
print("Bitwise NOT a:", result_not_a)  # Output: -16 (Binary: 11110000)
print("Bitwise NOT b:", result_not_b)  # Output: -8 (Binary: 11111000)

# Bitwise Left Shift
result_left_shift = a << 2
print("Bitwise Left Shift:", result_left_shift)  # Output: 60 (Binary: 111100)

# Bitwise Right Shift
result_right_shift = a >> 2
print("Bitwise Right Shift:", result_right_shift)  # Output: 3 (Binary: 11)
