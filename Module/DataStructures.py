'''
Created on Dec 17, 2018

@author: ksinha
'''

#LIST 
lang=['C','C++','Java','Python','COBOL','FORTRAN','JavaScript','VBScript']
print(lang)
print(type(lang))
del lang
#print(lang)


#TUPLE
a =(1,2,2,3)
b=(10,)
#k,l,m=a
print(a,b)
print(type(a),type(b))
print("TUPLE:",a.index(2),a.count(2))
#print(k,l,m)

#SET
myset={3,1,2}
print(myset)