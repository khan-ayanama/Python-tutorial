# MORE ABOUT LIST

# generate lists with range functions

# numbers = list(range(1, 11))
# print(numbers)


# index method --> gives the index of element
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]
# takes three arguments -->  first one is element to find,  second argument is from where to start searching and third is where to stop
ans = numbers.index(1, 3, 12)
print(ans)


# def negative_list(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#     return negative


# print(negative_list(numbers))
