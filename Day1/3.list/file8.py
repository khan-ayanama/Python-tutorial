# split method
# convert string to list


# split method
# user_info = "harshit,24".split(",")
# print(user_info)
# name, age = 'harshit,24'.split(',')
# print(name)
# print(age)

names = "Ayan Anand Aster Andrew"
print(type(names.split(" ")))  # here names will  turn into list
print(names)


# if you want to change string into list
# then use split method at the time of declaring the string not after that
# names = "Ayan Anand Aster Andrew".split(" ")
# print(names)


# join method  ---> Changes list into string
user_info = ["harshit", "24"]
ans = " ".join(user_info)
print(ans)
