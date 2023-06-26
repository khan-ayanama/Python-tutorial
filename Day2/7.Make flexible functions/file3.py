# Args as argument

# def multiply_nums(*args):
#     mul = 1
#     for i in args:
#         mul *= i
#     return mul


# nums = [1, 2, 3, 4]
# print(multiply_nums(*nums))  # *nums will unpack nums


# ##############    HW  ############

# power of elements to num in function

def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "You didn't pass any args"


nums = [1, 2, 3]
print(to_power(2, *nums))
