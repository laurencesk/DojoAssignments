class Store(object):
    def __init__(self,products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner
        self.inventory()
    def add_product(self,product):
        self.products.append(product)
        return self
    def remove_product(self,product):
        self.products.remove(product)
        return self
    def inventory(self):
        print self.products,self.location,self.owner
        return self

instance = Store(["meat","milk","cookies"],"seattle","laurence")
instance.add_product("veggie").remove_product("meat").inventory()
