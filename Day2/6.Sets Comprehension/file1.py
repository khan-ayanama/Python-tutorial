# sets comprehension

s = {k**2 for k in range(1, 11)}
print(s)
print(type(s))

s = 'ayan'
print(s)

names = ['Ayan', 'Naeem', 'Jameel', 'Alfred']
first = {name[0] for name in names}
print(first)
