# We use enumerate function with for loop to track position of our element
# item are iterable

# How can we do this without enumerate function
# names = ['abc', 'abcdef', 'Ayan']
# pos = 0
# for name in names:
#     print(f"{pos} --> {name}")
#     pos += 1


# With enumerate function
names = ['abc', 'abcdef', 'Ayan']

# ans = list(enumerate(names))  # It will return tuple
# print(ans)
# print(type(ans[0]))

# for pos,name in enumerate(names):
#     print(f"{pos} --> {name}")


# Define a function that take two arguments
# 1.) list containing string
# 2.) string that want to find in your list
# and this function will return the index of string in your list and
# if string is not present then return -1

def find_pos(l, target):
    for pos, name in enumerate(l):
        if name == target:
            return pos
    return -1


# print(find_pos(names, 'Ayan'))
# print(find_pos(names, 'Aydan'))

print(list(enumerate(names)))
