# polymorphism


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
