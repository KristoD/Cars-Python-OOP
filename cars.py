class Cars(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    
    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed) + "mph"
        print "Fuel: " + self.fuel
        print "Mileage: " + str(self.mileage) + "mpg"
        if self.price < 10000:
            self.tax = 0.12
        else:
            self.tax = 0.15
        print "Tax: " + str(self.tax)
        return self

car1 = Cars(2000, 35, "Full", 15)
car2 = Cars(2000, 5, "Not Full", 105)
car3 = Cars(2000, 15, "Kind of Full", 95)
car4 = Cars(2000, 25, "Full", 25)
car5 = Cars(2000, 45, "Empty", 25)
car6 = Cars(20000000, 35, "Full", 15)

print car1.display_all()
print car2.display_all()
print car3.display_all()
print car4.display_all()
print car5.display_all()
print car6.display_all()
