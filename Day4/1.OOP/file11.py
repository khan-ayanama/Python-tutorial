# Encapsulation
# Abstraction
# some special naming convention
# Name Mangling, __name  (not a convention)


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        # self._price = price
        self.__price = price

        def make_a_call(self, phone_number):
            print(f"calling {phone_number}....")

        def full_name(self):
            return f"{self.brand} {self.model_name}"

        def send_message(self):
            pass

# Encapsulation ----> Writing data and method at one place

# Abstraction --->  hiding complexity from the user

# l = [2, 3, 1, 2]
# l.sort()    # tim sort
# print(l)


# _name  # convention of private name
# __name__  # dunder/magic method

# Name Mangling

phone1 = Phone('nokia', '1100', 1000)
# print(phone1._price)
# phone1._price = 2000
# print(phone1._price)

# print(phone1.__dict__)
# print(phone1.__price)
print(phone1._Phone__price)
