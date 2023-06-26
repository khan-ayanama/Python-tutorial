# Excercise 2

class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def apply_discount(self, discount):
        return f"Discounted price {self.price - (self.price*discount/100)}"


laptop1 = Laptop('Asus', 'X441UA', 27000)

print(laptop1.model_name)
print(laptop1.apply_discount(50))
