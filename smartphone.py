class Smartphone:

    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def sayPhone(self):
        print(self.brand, '-', self.model, '-', self.number)