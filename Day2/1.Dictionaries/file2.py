# in keyword and iteration in dictionary

user_info = {
    'name': 'Ayan',
    'age': 20,
    'fav_movies': ['eye in the sky', 'interstellar']
}


# check if key exist in dictionary
# if 'name' in user_info:
#     print("present")
# else:
#     print('not present')


# Also gives the value of dictionaries
# print(user_info.values())


# .keys() gives the key of dictionaries
# print(user_info.keys())


# check if value exist in dictionary
# if 'Ayan' in user_info.values():
#     print("present")
# else:
#     print('not present')


# loops in dictionaries
# for i in user_info:
#     print(i)

# for i in user_info.values():
    # print(i)


# values method returns of type dict_values type
# user_info_values = user_info.values()
# print(user_info_values)


# keys method
# user_info_keys = user_info.keys()
# print(user_info_keys)


# loops in dictionary
# for i in user_info:
#     print(user_info[i])


# items method  ----> It returns tuples in list
# Ans --> dict_items([('name', 'Ayan'), ('age', 20), ('fav_movies', ['eye in the sky', 'interstellar'])]

user_items = user_info.items()
print(user_items)
# print(type(user_items))


# for key, value in user_info.items():
#     print(f"key is {key} and value is {value}")
