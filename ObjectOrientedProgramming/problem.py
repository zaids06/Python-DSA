# parent class
class Person():
    def __init__(self,name,age)->None:
        self.name=name
        self.age=age
    def display(self)->str:
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,dob)->None:
        super().__init__(name,age)
        self.dob=dob
    def displayInfo(self):
        print(self.name,self.age,self.dob)

# child class


obj = Student("Rahul", 23, "16-03-2000")
obj.display()
obj.displayInfo()
