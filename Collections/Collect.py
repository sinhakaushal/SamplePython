'''
Created on Nov 30, 2018

@author: ksinha
'''
#s = input('ENTER STRINGS')
s ="HELLO MY NAME IS KAUSHAL SINHA ."
sparts=s.split(" ")
for s in sparts:
    print(s," ", len(s))

# RANGE    
for i in range(len(sparts)):
    print(i," ", sparts[i])
print(sparts)

a=range(10)
print(a)        