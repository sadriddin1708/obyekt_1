class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
    def chiqar(self):
        print(f'Mashina {self.brand} {self.color} rangda')

mashina = Car('Qizil', 'Mersedes')
#print(mashina.brand)
#print(mashina.color)

mashina.chiqar()