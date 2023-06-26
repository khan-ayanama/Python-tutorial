# NotImplementedError
# abstract error

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError(
            "you should define it in subclass you asshole")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


doggy = Dog('boony', 'pug')
print(doggy.sound())
