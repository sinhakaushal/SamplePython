'''
Created on Dec 21, 2018

@author: ksinha
'''

#INHERTIANCE
class Date(object):
    def get_date(self):
        return '2018-12-31'
class Time(Date):
    def get_time(self):
        return '13:00:36'
dt=Date()
tt=Time()
print(dt.get_date())
print(tt.get_time())
print(tt.get_date())    


#Multiple Inheritance
class A(object):
    def do_this(self):
        print("doing at A")
class B(A):
    pass
class C(object):
    def do_this(self):
        print("doing at C")
class D(C,B):
    pass
instance_d=D()
instance_d.do_this()
print(D.mro())

#Inhertance Diamond Shape
class AA(object):
    def do_this(self):
        print("doing at AA")
class BB(AA):
    pass
class CC(AA):
    def do_this(self):
        print("doing at CC")
class DD(CC,BB):
    pass
instance_dd=DD()
instance_dd.do_this()
print(DD.mro())
