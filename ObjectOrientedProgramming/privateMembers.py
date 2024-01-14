class Person:
    __addharno=""
    def __init__(self,aadharNo)->None:
        self.age =0
        self.name =""
        self.address=""
        self.__addharno=aadharNo
    def setAge(self,age):
        self.age = age
    def getAge(self):
        return self.age
    def getAddharno(self):
        return self.__addharno

person1=Person("123455")
print(person1.getAddharno())
