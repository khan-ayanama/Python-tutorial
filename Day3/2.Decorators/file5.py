# Decorators - enhance the functionality of other functions

# @ use for decorators

def decorator_function(any_function):
    def wrapper_function():
        print('this is awesome function')
        any_function()
    return wrapper_function


@decorator_function
def func1():
    print("this is function one")


func1()


@decorator_function
def func2():
    print("this is function two")


# func1()
# func2()
# var = decorator_function(func1)
# var()
