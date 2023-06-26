# readfile
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method

# 1.read file

f = open('file1.txt', 'r')

# print(f.readline(), end='')
# print(f.readline())

# print(f"cursor position {f.tell()}")

# print(f.read())

# print(f"cursor position {f.tell()}")
# f.seek(0)
# print(f"cursor position {f.tell()}")


# print(f.read())  # it will not print anything

lines = f.readlines()   # it will return list

# name of file
print(f.name)
print(f.closed)

print(lines)


f.close()
print(f.closed)
