# Add and Delete data from dictionaries

user_info = {
    'name': 'Ayan',
    'age': 20,
    'fav_movies': ['interstellar', 'wiplash']
}

# How to add data
# user_info['fav_song'] = 'Aarambh hai prachand'
# print(user_info)


# pop method
pop_item = user_info.pop('age')
print(user_info)
print(pop_item)


# popitem method --> Deletes randomly one keyvalue pair
# popped_item = user_info.popitem()
# print(popped_item)
# print(user_info)
