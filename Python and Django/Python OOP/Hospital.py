class Hospital(object):
    def __init__(self,name,capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
    def admit(self,patient):
        self.patients.append(patient)
        self.bedsAvailable = self.capacity-len(self.patients)
        return self
    def discharge(self,patient):
        self.patients.remove(patient)
        self.bedsAvailable = self.capacity-len(self.patients)
        return self
    def info(self):
        print self.name, self.capacity, self.bedsAvailable
        return self

class Patients(object):
    idNum = 1
    def __init__(self,name,allergies):
        self.idNum = Patients.idNum
        Patients.idNum +=1
        self.name = name
        self.allergies = ""
        self.bedNumber =1
    def assignBed(self):
        self.bedNumber = Hospital.bedsAvailable+1
        return self
    def patientInfo(self):
        print self.idNum, self.name, self.allergies, self.bedNumber
#
p1 =Patients("someone","medicine").patientInfo()
p2 =Patients("someone else","none").patientInfo()


hos1 = Hospital("The H",5).admit(p1).info()
