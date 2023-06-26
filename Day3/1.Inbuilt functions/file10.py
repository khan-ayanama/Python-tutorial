# l = [1, 2, 3, 4, 5]
# l = [8, 2, 2, 4, 6]
# even = (all(map(lambda a: a % 2 == 0, l)))
# print(even)

# names = ['Ayan', 'Jameel', 'Naeemullah', 'Gaurav']

# ans = max(names, key=lambda name: len(name))
# print(ans)

student1 = [
    {'Name': 'Harshit', 'Score': 90, 'age': 24},
    {'Name': 'Mohit', 'Score': 70, 'age': 20},
    {'Name': 'Rohit', 'Score': 100, 'age': 28}
]

max_score = max(student1, key=lambda item: item['Score'])['Name']
print(max_score)
