class Adress:
 
    def __init__(self, index, city, street, house, flat):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat
    
    def say_to_adress(self):
        print(self.index + ',', self.city + ',',  self.street + ',', self.house, '-', self.flat)

    def say_from_adress(self):
        print('в', self.index + ',', self.city + ',', self.street + ',', self.house, '-', self.flat, '.')

