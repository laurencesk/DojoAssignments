class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.display_all()
    def tax(self):
        if self.price >10000:
            return "15%"
        else:
            return "12%"
    def display_all(self):
        print self.price, self.speed,self.fuel,self.mileage,selft.tax()

car1 = Car(2000,"35mpg","Full","15mpg")
