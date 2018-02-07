class call(object):
    def __init__(self,uniqueId,name,number, time, reason):
        self.uniqueId = uniqueId
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
        # self.display()
    def display(self):
        print self.uniqueId, self.name,self.number,self.time,self.reason


class callCenter(object):
    def __init__(self):
        self.calls = []
        self.queueSize=0
    def add(self,call):
        self.calls.append(call)
        self.queueSize = len(self.calls)
        return self
    def remove(self):
        self.calls[0].remove()
        return self
    def info(self):
        print self.queueSize
        for call in self.calls:
            print call.display()
        return self

callCenter1 = callCenter()
callCenter1.add(call(123,"laurence",123,"02/06","no reason")).add(call(456,"laurence",321,"02/06","no reason")).info()
