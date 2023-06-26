# ##############    HOMEWORK    #####################

# 1.Function which will return the square of list elements

# numbers = [1, 2, 3, 4, 5, 6]
# l = []


# def square(number):
#     for num in number:
#         print(num)
#         # l.insert(num-1, num**2)  # OR
#         l.append(num**2)
#     return l


# print(square(numbers))


# 2.Reverse the list

# numbers = [1, 2, 3, 4, 5, 6]

# Method 1
# numbers.reverse()
# print(numbers)

# Method 2
# name = 'Ayan'
# print(numbers[::-1])


# Method 3
# count = len(numbers)
# l = []
# for i in range(count):
#     l.append(numbers.pop())

# print(l)

# 3.reverse the string in list

names = ['ABC', 'DEF', 'GHI']


def reverse_names(name):
    for i in name:
        return name[::-1]


print(reverse_names(names))

# 4.Filter odd and even from list and then append it in the bigger  list

# numbers = [1,2,3,4,5,6,7,8,9]
# odd_nums = []
# even_nums = []

# def odd_even_nums(number):
#     for i in number:
#         if i%2==0:
#             even_nums.append(i)
#         else:
#             odd_nums.append(i)
#     output = [even_nums,odd_nums]
#     return output

# ans = odd_even_nums(numbers)
# print(ans)


# 5. Common elements in lists

# def common_finder(l1,l2):
#     output = []
#     for i in l1:
#         if i in l2:
#             output.append(i)
#     return output

# print(common_finder([1,2,3,4],[3,4,5,6]))


# 6. numbers of list in list

# def list_count(l):
#     count = 0
#     for i in l:
#         if type(i) == list:
#             count += 1
#     return count


# print(list_count([12, 3, [12, 3, 4], [5, 3, 3], [2]]))
