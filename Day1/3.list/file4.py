# Add data to list
# APPEND METHOD, INSERT METHOD, CONCAT LISTS, EXTEND METHOD


# #############     APPEND METHOD   ###############
fruits = ["grapes", "apple"]
# fruits.append("mango")  # Add items to last
# print(fruits)


# More methods to add data in list

fruits1 = ["mango", "apple"]

# INSERT METHOD ---> Add items at given position and pushes back the previous value

# fruits1.insert(1, "grapes")
# print(fruits1)


# concatenate two lists

fruits2 = ["grapes", "apple"]
# fruits = fruits1 + fruits2
# print(fruits)


# extend method  ---> change the original value and spread the values at last
# fruits1.extend(fruits2)
# print(fruits1)
# print(fruits2)

# If we append to list then the list will be inside the parent list
# fruits1.append(fruits2)
# print(fruits1)


# ######### Delete data from list   ###########
# POP METHOD, Del OPERATOR, REMOVE OPERATOR

fruits = ["orange", "apple", "pear", "banana", "kiwi", "banana"]

# pop() method

# fruits.pop()    # Pops item from behind and also returns popped value
# print(fruits)
# fruits.pop(2) # pops value at given index
# print(fruits)


# delete operator, It deletes the value of given index but does not return
# del fruits[1]
# print(fruits)


# remove method, It removes but doesn't returns the removed value
removed_item = fruits.remove('banana')
# print(removed_item)
print(fruits)
# fruits.remove('patanahi')
