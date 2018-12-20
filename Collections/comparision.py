'''
Created on Dec 19, 2018

@author: ksinha
'''

#compare two Tuple - Since Data retrieved from DB is in form of Tuple. Better use below.
tup1=(101,103,105,107,108)
tup2=(101,103,106,107,108,109)
#tup21=tup2-tup1
#print(tup21)
extra_t_tuple=() # Store diff in Tuple
extra_t_dict={}   #Store diff in Dictionary
for i in tup1:
        if i not in tup2:
            print(i,"  Not FOUND")
            extra_t_tuple=extra_t_tuple+(i,)
            extra_t_dict[i]="tup1"
for j in tup2:
    if j not in tup1:
        print(j,"Not Found")
        extra_t_tuple=extra_t_tuple+(j,)
        extra_t_dict[j]="tup2"
print(extra_t_tuple)
print(extra_t_dict)

print("========****************************===============")
#Compare Two List
lst1=[101,103,105,107,108]
lst2=[101,103,106,107,109]
extra_l_dict={}   #Store diff in Dictionary
extra_l_list=[]     #Store diff in list
for i in lst1:
        if i not in lst2:
            print(i,"  Not FOUND")
            extra_l_list.append(i)
            extra_l_dict[i]="List1"
for j in lst2:
    if j not in lst1:
        print(j,"Not Found")
        extra_l_list.append(j)
        extra_l_dict[j]="list2"
print(extra_l_list)
print(extra_l_dict)



print("=========================================================")
#Compare Dictionary
dict1={1:"Kaushal",2:"Rahul",3:"Rohit","104":"Namesake"}
dict2={4:"Devina",3:"Kunal",2:"Rahul","106":"No Entry",104:"Namesake"}
#in operator is being used to check the key only
missing_dict={}
for i in dict1:
    if i in dict2:
        if dict1[i]==dict2[i]:
            print(i," Found and Matched")
        else:
            print(i, " Found but not matched")
            missing_dict[i]=dict1[i]   
    else:
        print(i," is Missing")
        missing_dict[i]=dict1[i]
#print("Missing dictionary:", missing_dict)        
for i in dict2:
    if i in dict1:
        if dict2[i]==dict1[i]:
            print(i," Found and Matched")
        else:
            print(i, " Found but not matched")
            missing_dict[i]=dict2[i]   
    else:
        print(i," is Missing")
        missing_dict[i]=dict2[i]
print("Missing dictionary:", missing_dict)