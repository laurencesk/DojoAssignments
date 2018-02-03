class bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self
    def ride(self):
        self.miles += 10
        print 'Riding'
        return self

    def reverse(self):
        self.miles -=5
        print 'Reversing'
        return self


bike1 = bike(200,"25mpg",0)
bike2 = bike(150,"20mpg",0)
bike3 = bike(300,"35mpg",0)
