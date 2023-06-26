class Mobile:
    def __init__(self, name):
        self.name = name


class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, new_mobile):
        self.mobiles.append(new_mobile)


oneplus = Mobile('one plus 6')
samsung = 'samsung galaxy s8'
mobostore = MobileStore()

# print(mobostore.mobiles)
mobostore.add_mobile(samsung)
