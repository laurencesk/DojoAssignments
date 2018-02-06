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
        print self.price, self.speed,self.fuel,self.mileage,self.tax()

car1 = Car(2000,"35mpg","Full","15mpg")
car2 = Car(2000,"5mpg","Not Full","105mpg")
car3 = Car(2000,"15mpg","Kind of Full","95mpg")
car4 = Car(2000,"25mpg","Full","25mpg")
car5 = Car(2000,"45mpg","Empty","25mpg")
car6 = Car(20000000,"35mpg","Empty","15mpg")
