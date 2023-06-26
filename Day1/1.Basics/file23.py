# Counting the character when some are in UPPER CASE and some ae in lower case

name, char = input("Enter name and char ").split(",")

print(f"length of your name is {len(name)}")
print(f"character count : {name.count(char)}")

# First make a name and chare in lower and then cound all the character
name.lower()
char.lower()

print(f"character count : {name.lower().count(char.lower())}")


# PRACTICE EXCERSCISE
# name = "Ayan KhAn"
# print(name.lower().count("a"))
# print(name)
# print(name.count("a"))
