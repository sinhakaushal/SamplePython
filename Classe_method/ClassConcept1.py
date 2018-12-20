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

#__init Constructor
class class3(object):
    def  __init__(self,a,b):
        self.aa=a
        self.bb=b
x=class3(4,5)
print("aa=",x.aa,"||bb=",x.bb)
x.aa=44
x.bb=55
print("aa=",x.aa,"||bb=",x.bb)

#Overriding the attribute
class class4(object):
    a=4
y=class4()
print(y.a)
y.a=44
print(y.a)
del y.a
print(y.a)
#del y.a
#print(y.a) # Gives error as no value is there in Attribute a "AttributeError: a"


#Working with Class and Instance Data
class myClass:
    class_attribute = 99
    def class_method(self):
        self.instance_attribute = 'I am instance attribute'
print (myClass.__dict__)
### ====== STILL TO EXPLORE ABOVE CLASS ############===============
    
       
        