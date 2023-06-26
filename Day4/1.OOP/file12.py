# will discuss three problems in existing
# then we will solve them using getter, setter decorato

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        # How to solve a problem of negative price
        self._price = max(price, 0)

        # self.complete_specification = f"{self.brand} {self.model_name} and price is {self._price} "

        @property   # it will change from function to property
        def complete_specification(self):
            return f"{self.brand} {self.model_name} and price is {self._price} "

    # getter(), seteter()
        @property
        def price(self):
            return self._price

        @price.setter
        def price(self, new_price):
            self._price = max(new_price, 0)

        def make_a_call(self, phone_number):
            print(f"calling {phone_number}....")

        def full_name(self):
            return f"{self.brand} {self.model_name} "


# How to solve a problem of negative price

phone1 = Phone('Nokia', '1100', -1000)
print(phone1.brand)
print(phone1.model_name)
print(phone1._price)
# how to print updated complete sequence
# print(phone1.complete_specification)
print(phone1.complete_specification())
