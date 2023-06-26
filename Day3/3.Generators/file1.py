# Generators
# generators are iterators

# l = [1,2,3]

# Generators generate one element at one time it takes less time and space


# Create first generator with generator function
# 1.) generator function
# 2.) generator comprehnsion


# Generator Function

# with normal sequence
# def nums(n):
#     for i in range(1, n+1):
#         print(i)


# nums(10)

# with generator
def nums(n):
    for i in range(1, n+1):
        yield (i)


numbers = nums(10)

for num in numbers:
    print(num)

# you can use only once in generators
for num in numbers:
    print(num)
