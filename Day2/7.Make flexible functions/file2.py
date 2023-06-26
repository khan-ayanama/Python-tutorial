# *args with normal parameter

# when normal arguement you have to pass the parameter otherwise it will give an error
def multiply_nums(num, *args):
    print(num)
    mul = 1
    for i in args:
        mul *= i
    return mul


# here first argument will be assigned to num and rest to the args in the form of tuple
print(multiply_nums(2, 3, 3, 4, 5))
