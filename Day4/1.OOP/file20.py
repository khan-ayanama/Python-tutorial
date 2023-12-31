# Special magic method / dunder methods
# operator overloading
# polymorphism


# Special magic method / dunder method

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f"{self.brand} {self.model}"

    # str, repr

    def __str__(self):
        return f"{self.brand} {self.price}"

    def __repr__(self):
        return f"Phone(\'{self.brand}\',{self.model},{self.price})"

    def __len__(self):
        return len(self.phone_name())


my_phone = Phone('Nokia', '1100', 1000)
# print(my_phone)
# print(str(my_phone))
# print(repr(my_phone))
# print(my_phone.__repr__())
