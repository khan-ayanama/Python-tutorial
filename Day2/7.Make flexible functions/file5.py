# function with all type of operators
# very important to understand

# PADK

# parameters
# *args (Arguments)
# Default parameters
# **kwargs

# order of parameter
# def func(name, *args, last_name='unknown', **kwargs):
#     print(name)
#     print(args)
#     print(last_name)
#     print(kwargs)


# func('Ayan', 1, 2, 3, a=1, b=2)


# ############  H.W.    ###########

def func(l, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]


names = ['ayan', 'howard', 'sheldon']
print(func(names, reverse_str=True))
