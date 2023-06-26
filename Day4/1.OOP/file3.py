# Excerse of class

class Laptop:
    def __init__(self, brand_name,model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
    

laptop1 = Laptop('Asus','X441UA',2700)

print(laptop1.model_name)