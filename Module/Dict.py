'''
Created on Dec 18, 2018

@author: ksinha
'''
from builtins import sorted

my_dict={x*x:x for x in range(5)}
print(my_dict)
print(my_dict[4])
print(my_dict.get(16))
print("DICTIONARY 2 Example")
my_dict2={1:"Kaushal",2:"Amit",3:"Ratnesh",4:"Ashish",5:"Abhishek",6:"Priya",7:"Khusbhu",8:"Piyali"}
print(my_dict2)

#Updating Dictionary
my_dict2[7]="Khusbhoo"
print(my_dict2)
#addding element in dictionary
my_dict2[0]="Pattric"
print(my_dict2)
print("KEYS ONLY",my_dict2.keys(),"TYPE:",type(my_dict2.keys()))
print(my_dict2.values())

#PRINTING DICTIONARY
for key,value in sorted(my_dict2.items()):
    print(key,"|",value)
for name in my_dict2:
    print(name,"||",my_dict2[name])

#Delete dictionary
del my_dict[0]
print(my_dict)
del my_dict
##print(my_dict)

#Inbuilt Function
print(len(my_dict2))
print(sorted(my_dict2))
print(1 in my_dict2)
mdict={1:1,2:3,4:5}
ndict={1:1,2:2,3:3}
print(any(mdict),"||",any(ndict))
print(all(mdict),"||",all(ndict))

my_dict2_item=my_dict2.items()
print(type(my_dict2_item),"||",my_dict2_item)

#Operation in Dictionary
dict2={x: x for x in range(10)}
dict3={}
print("DICT2:",dict2)
print("Dict3:",dict3)
dict3=dict2.copy()
print("new dict3",dict3)
for i in dict2:
    dict3[i]=dict2[i]*5
print("5 dict3",dict3)
a=[1,"Bihar",2,"Jharkhand",3,"West Bengal",4,"Odisha",5,"Uttar Pradesh",6,"Madhya Pradesh",7,"Chattisgarh"]
b = {a[i]: a[i+1] for i in range(0, len(a), 2)}
print(b)
#Creating dictionary using List + tuple
ne_states=["Assam","Tripura","Nagaland","Arunachal pradesh","Manipur","Meghalaya","Mizoram"]    #list
ne_code=(101,105,107,109,110,111,187)   #Tuple
print(sorted(ne_states))

dict_ne_states={i:ne_states[i] for i in range(0,len(ne_states))}
print(max(len(ne_states),len(ne_code)))

dict_ne_states_code={ne_code[i]:ne_states[i] for i in range(0,max(len(ne_states),len(ne_code)))}
print(dict_ne_states_code)

#Nested Dictionary
"""
Can be used to store the data from Json file
"""

    