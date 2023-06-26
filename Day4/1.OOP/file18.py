# isinstance

# base/parent class
class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)

    def make_a_call(self, phone_number):
        print(f"calling {phone_number}....")

    def full_name(self):
        return f"{self.brand} {self.model_name} "


# derived/Child class
class Smartphone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"


class FlagshipPhone(Smartphone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera


oneplus5 = Smartphone('onePlus', '5', 30000, '6 GB', '64 GB', '20 MP')
oneplus5t = FlagshipPhone('onePlus', '5', 30000, '6 GB',
                          '64 GB', '20 MP', '16 MP')

# isinstance --> kya ye instance hai
# print(isinstance(oneplus5, Smartphone))
# print(isinstance(oneplus5, Phone))

# print(isinstance(oneplus5t, Phone))
# print(isinstance(oneplus5, FlagshipPhone))


# ########## issubclass #############

print(issubclass(Smartphone, Phone))
print(issubclass(Smartphone, Smartphone))
