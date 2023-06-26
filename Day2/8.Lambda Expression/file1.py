# lambda expressions (anonymous function)

def add(a, b):
    return a+b


def add2(a, b): return a+b


print(add2(2, 3))


def multiply(a, b): return a*b


print(multiply(5, 6))

# lambda function has no name
print(add)
print(add2)

input = [1, 2, 3, 4, 5]

output = list(map(lambda x: x**2, input))
print(output)
