# zip function
# zip function can work with any number of lists
# when more than two lists zipped then you can't change it into dictionary

user_id = ['user1', 'user2', 'user3']
names = ['harshit', 'mohit', 'rohit']

# ('user1','harshit'),('user2','mohit')

print(list(zip(user_id, names)))
# Answer of above
# [('user1', 'harshit'), ('user2', 'mohit'), ('user3', 'rohit')]


# Tuples to dictionary
# example = [('a', 1), ('b', 2)]
# print(dict(example))


# * operator with zip
# l1 = [1, 3, 5, 7]
# l2 = [2, 4, 6, 8]

# l = [(1, 2), (3, 4), (4, 5)]

# print(list(zip(*l)))
# l1, l2 = list(zip(*l))
# print(list(l1))
# print(l2)

# new_list = []

# for pair in zip(l1, l2):
#     new_list.append(max(pair))

# print(new_list)
