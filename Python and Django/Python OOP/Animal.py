class animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -=1
        return self
    def run(self):
        self.health-=2
        return self
    def display(self):
        print self.health
        return self
class dog(animal):
    def set_health(self):
        self.health = 150
        return self
    def pet(self):
        self.health +=5
        return self
class dragon(animal):
    def set_health(self):
        self.health = 170
        return self
    def fly(self):
        self.health -=10
        return self
    def display(self):
        print self.name, self.health
        return self

Animal = animal("abc",100).walk().walk().walk().run().run()
Animal.display()

dog1 = dog("abc",100).set_health().pet().display()
dragon1 = dragon("abc",100).set_health().fly().display()
