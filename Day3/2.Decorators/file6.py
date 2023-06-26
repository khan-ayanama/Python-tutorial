from functools import wraps


def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        '''this is wrapper function'''
        print('this is awesome function')
        return any_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def func1(a):
    print(f"this is function with argument {a}")


# func1(7)


@decorator_function
def add(a, b):
    ''' this is add function'''
    return a+b


print(add(2, 3))
# print(add.__doc__)
