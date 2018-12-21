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
    