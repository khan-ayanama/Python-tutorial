# Dictionary comprehension with if else
odd_even = {i: ('even' if i % 2 == 0 else 'odd') for i in range(1, 8)}
print(odd_even)
