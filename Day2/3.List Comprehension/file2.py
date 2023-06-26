# List comprehension with if statment

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# printing even numbers in numbers list
# even_num = [i for i in numbers if i % 2 == 0]
# print(even_num)


# odd_num = [i for i in numbers if i % 2 != 0]
# print(odd_num)


# list comprehension with if else statement

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = [i*2 if (i % 2 == 0) else -i for i in nums]
# print(new_list)


# list comprehensin in nested list

# example = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

nested_comp = [[i for i in range(1, 4)] for j in range(3)]
print(nested_comp)
