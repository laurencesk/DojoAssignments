class MathDojo(object):
    def __init__(self,):
        self.total = 0
    def add(self,*para):
        for i in range(0,len(para)):
            if type(para[i]) is list or type(para[i]) is tuple:
                for j in range(0,len(para[i])):
                                self.total+=para[i][j]
            else:
                self.total+=para[i]
        return self
    def subtract(self,*para):
        for i in range(0,len(para)):
            if type(para[i]) is list or type(para[i]) is tuple:
                for j in range(0,len(para[i])):
                                self.total-=para[i][j]
            else:
                self.total-=para[i]
        return self
    def result(self):
        print self.total

md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
