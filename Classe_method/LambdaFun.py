'''
Created on Dec 14, 2018

@author: ksinha
'''

x=lambda :print("Hello World")
x()

x=lambda a,b:a*b
print(x(3,4))

def myfunc(n):
    return lambda a : a*a * n
mydoubler = myfunc(11) #Value Assigned to n
print(mydoubler(2)) # Value assigned to a i.e. lambda

