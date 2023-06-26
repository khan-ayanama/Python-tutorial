# operator overloading

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

    def __add__(self, other):
        return self.price + other.price


my_phone = Phone('Nokia', '1100', 1000)
my_phone2 = Phone('Nokia', '1600', 1600)
print(my_phone+my_phone2)
