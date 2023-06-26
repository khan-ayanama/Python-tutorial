# Read with block
# context manager
# It will automatically close the file --> not need to use close() method

with open('file1.txt') as f:
    data = f.read()
    print(data)
