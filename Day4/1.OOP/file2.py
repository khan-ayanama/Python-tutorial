# Objective
# What is Class
# How to create an class
# what is init method/ constructor method as in javascript
# What are attributes, instance variables
# How to create our object


class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


p1 = Person('Ayan', 'Khan', 20)
p2 = Person('Harshit', 'Vasistha', 24)

print(p1.first_name)