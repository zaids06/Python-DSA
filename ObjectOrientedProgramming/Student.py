class Student:
    def __init__(self)->None:
        self.name=""
        self.marks=[]
        self.address=""

    def setName(self,name):
        self.name=name
    def setMarks(self,marks):
        self.marks.append(marks)
    def setAddress(self,address):
        self.address=address
    def getAverage(self):
        return sum(self.marks)/len(self.marks)

s1=Student()
s2=Student()
s1.setName("Zaid")
s1.setMarks(20)
s1.setMarks(30)
print(s1.getAverage())