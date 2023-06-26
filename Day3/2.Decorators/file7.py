# Decorator function practice

# from functools import wraps


# def print_function_data(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         print(f"you're calling {function.__name__}")
#         print(f"{function.__doc__}")
#         return function(*args, **kwargs)
#     return wrapper


# @print_function_data
# def add(a, b):
#     '''THis function takes two numbers and returns sum'''
#     return a+b


# print(add(4, 5))


# ###############   Home Work   #############

# Time taken by function
# import time

# t1 = time.time()
# print("Hello")
# t2 = time.time()
# print(t2 - t1)


from functools import wraps

import time


def calculate_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"executing....{function.__name__}")
        t1 = time.time()
        returned_value = function(*args, **kwargs)
        t2 = time.time()
        total_time = t2 - t1
        print(f"this function took {total_time} seconds")
        return returned_value
    return wrapper


@calculate_time
def square_finder(n):
    return [i**2 for i in range(1, n+1)]


square_finder(100000)
