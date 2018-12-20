'''
Created on Dec 17, 2018

@author: ksinha
'''
from collections import Counter
cd= Counter('Hello')
print(cd)
cd.update('Hello Once AGain')
print(cd,"|",cd.most_common(2))
print(cd['H'])

mylist=['India','Austraila','UK','China','Nepal']
mydict=Counter(mylist)
print(mydict)