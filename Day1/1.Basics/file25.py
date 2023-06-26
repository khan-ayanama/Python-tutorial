# replace() method
# find() method

string = "she is beautiful and she is good is dancer"
print(string.replace(" ", "_"))
print(string.replace("is", "was", 3))


# find() method

print(string.find("is"))
print(string.find("is", 6))
is_pos1 = string.find("is")  # is_pos1 ---> number
is_pos2 = string.find("is", is_pos1+1)
print(is_pos2)
