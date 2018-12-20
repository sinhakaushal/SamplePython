'''
Created on Dec 12, 2018

@author: ksinha
'''
class Vechicle:
    """Let Create a Class for Practise"""
    color="red"
    def __init__(self,kind):
        self.kind=kind
        #return "HEllo Method calling"
print(Vechicle.color)
c=Vechicle("Car")
a=Vechicle("Auto Rickshaw")
print(a.color,"||",a.kind)
print(c.color,"||",c.kind)
a.color="Black"
print(a.color,"||",a.kind)
print(c.color,"||",c.kind)
Vechicle.color="Blue"
print(Vechicle.color)
print(a.color,"||",a.kind)
print(c.color,"||",c.kind)
#print(x.f())
#xf=x.f
#print(xf())
