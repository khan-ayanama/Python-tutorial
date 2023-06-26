# list comprehension
# with the help of list comprehension we can create list in one line

# Creat a list of squares from 1 to 10

# normal method
# squares = []
# for i in range(1, 11):
#     squares.append(i**2)
# print(squares)

# List comprehension method
# square2 = [i**2 for i in range(1, 11)]
# print(square2)

# Creating a list of negative number from 1 to 10
# negative_numbers = [-i for i in range(1, 11)]
# print(negative_numbers)

# Create a list of first character of name string
names = ['Ayan', 'Naeem', 'Mohit']
# first_char = [names[0] for i in names]
first_char = [name[0] for name in names]
# print(first_char)

first_character = [name[0] for name in names]
print(first_character)
