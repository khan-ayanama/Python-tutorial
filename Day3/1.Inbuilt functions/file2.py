# map function
# list is an iteratorra
numbers = [1, 2, 3, 4]

# map is an iterator
# square of a list
squares = list(map(lambda a: a**2, numbers))
print(squares)


# length of string
names = ['abc', 'abcd', 'abcde']
length = list(map(len, names))
print(length)
