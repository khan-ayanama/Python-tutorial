# compare list
# is vs equal(==)

fruits1 = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
fruits2 = ["banana", "fruit2"]
fruits3 = ["banana", "fruit2"]

print(fruits1 == fruits2)
print(fruits2 == fruits3)  # if value is same or not not calculate address

print(fruits2 is fruits3)  # Checks values are at same address
