# Dictionary Comprehension

# Create a dictionary of square of key
# square = {i: i**2 for i in range(1, 4)}
# print(square)

# 2nd method
square = {f"square of {i}: {i**2}" for i in range(1, 4)}
print(square)
