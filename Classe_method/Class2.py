'''
Created on Dec 14, 2018

@author: ksinha
'''
class Student:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    def tellName(self):
        print("Name is "+self.name)
        print("Name is "+self.gender)   
p1=Student("Kaushal","Male")        
p1.tellName() 