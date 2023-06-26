# class method as constructor


# class methods
# difference between class methods and instance methods

class Person:
    count_instance = 0  # class variables / class attributes

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(',')
        return cls(first, last, age)

    @classmethod
    def count_instances(cls):
        return f"You've created {cls.count_instance} instance method"

    # Creating own instance method

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age > 18


p1 = Person('Ayan', 'Khan', 20)
p2 = Person('Naeem', 'Holland', 19)

# calling class method
p3 = Person.from_string('Ayan,khan,20')
print(p3.full_name())
