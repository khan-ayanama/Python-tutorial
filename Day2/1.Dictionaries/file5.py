# fromkeys method ---> It is used to create a dictionary

# d = dict.fromkeys(['name', 'age', 'height'], 'unknown')
# d2 = dict.fromkeys(('name', 'age', 'height'), 'unknown')
# d3 = dict.fromkeys("abc", 'unknown')
# d4 = dict.fromkeys(range(1, 11), 'unknown')
# print(d)
# print(d2)
# print(d3)
# print(d4)


# get method ---> Get method is used to handle error when key is not available in the dictionaries
# d = {'name': 'unknown', 'age': 'unknown'}
# print(d['gender'])
# print(d.get('gender'))  # It will give an answer none not an error
# print(d.get('gender','who'))  # It can also give customize error

# clear method ---> It clears a dcitionray
# dict1 = {'name': 'unknown', 'age': 'unknown'}
# dict1.clear()
# print(dict1)

# copy method  ---> copy the dictionary
# dict2 = {'name': 'unknown', 'age': 'unknown'}
# new_dect = dict2.copy()
# print(new_dect)
