class product(object):
    def __init__(self,price,itemName, weight,brand,status):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand  = brand
        self.status = status
        self.addTax()
        self.Return()
        self.display()
    def sell(self):
        self.status = "sold"
        return self
    def addTax(self):
        tax =0.101
        return self.price*(1+tax)
    def Return(self):
        if self.status == "defective":
            self.status = "defective"
            self.price = 0
        if self.status =="like new":
            self.status = "for sale"
            self.price = 0
        if self.status =="used":
            self.status = "used"
            self.price = self.price*0.8
        return self
    def display(self):
        print self.price, self.itemName, self.weight, self.brand,self.status
        return self

product1 = product(1000,"name",50,"brandName","used")
