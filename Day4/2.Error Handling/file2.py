# Raise errors

def add(a, b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError('OOPs you are douchebag entering wrong dataype')


print(add('a', 'b'))
