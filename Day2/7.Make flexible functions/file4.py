# kwargs (keyword arguments)
# **kwargs (double star operators)

# kwargs as parameter
def func(**kwargs):
    print(kwargs.items())
    for k, v in kwargs.items():
        print(f"{k}:{v}")


# func function will change the input into dictionary
# func(first_name='Ayan', last_name='Khan')


# Dictionary unpacking
d = {'name': 'Ayan', 'age': 20}
func(**d)
