# debugging in python

import pdb

# steps for debugging
# 1.) set trace
# 2.) execute code line by line

pdb.set_trace()
name = input('Enter name ')
age = input('Enter age')

print(f'hello{name} your age {age}')
age2 = age + 5
print(f'{name} you will be {age2} in 5 years')

# l ---> To know where is set_trace
# c ----> continue without stopping
# q ----> quit debugging
# n ----> move to next line
