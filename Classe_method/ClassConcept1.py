'''
Created on Dec 20, 2018

@author: ksinha
'''
class classconcept1():
    var=9
    def firstPrint(self):
        print("Hello Print 1")
        print(self)
obj=classconcept1()
print(obj)
print(obj.var)
obj.firstPrint()
print(obj)

#Encapsulation- Hide Complexity by using Getter & Setter
class class2(object):
    def setAge(self,age):
        self.age=age
    def getAge(self):
        return self.age
priya=class2()
priya.setAge(29)
print(priya.getAge())
priyanka=class2()
priyanka.setAge("Twenty Nine")
print(priyanka.getAge())           
        