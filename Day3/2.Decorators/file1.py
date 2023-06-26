# You have to have a complete understanding of functions
# first class function /closures
# then finally we will learn about decorators

def square(a):
    return a**2


s = square

# After assigning s equals to function now you can call it
print(s(3))
print(s.__name__)
