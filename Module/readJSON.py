'''
Created on Dec 18, 2018

@author: ksinha
'''
import sys
import json
print("Hello World")
try:
    file=open("input.json", "r")
except IOError:
    print("There was an error reading file")
    sys.exit()
file_text=file.read()
print(file_text)
file.close()
file21=json.loads(file_text)
print(type(file21))
print("LIST PRINTING")
file2=file21
'''
file2={}
def merge(m1,m2):
    m1.update(m2)
    return m1
for j in range(0,len(file21)):
    print(file21[j])
    file2=merge(file2,file21[j])
    abc=len(file2)
    print(abc)
'''    
    #file2.update(file21[j])
#file2=file21[1]

print(type(file2))
for i in file2:
    print(i,"||",file2[i])
    
for p_id, p_info in file2.items():
    print("\nPerson ID:", p_id)
    for key in p_info:
        #print(type(p_info))
        print(key ,":", p_info[key],"||",type(p_info))