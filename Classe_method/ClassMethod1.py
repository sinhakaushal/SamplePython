'''
Created on Dec 20, 2018

@author: ksinha
'''
lst=[101,102,103,104,105]
print("lst: ",lst)
#reverse() and len()
print("len(lst):",len(lst),"||lst.__len__():",lst.__len__())
lst1=lst
lst.reverse() #this reverse the list
print(lst)

#Reversed()-It returns the reverse iterator
lst1=reversed(lst)
for i in lst1:
    print(i)


class CustomSequence():
    def __len__(self):
        return 5
    def __getitem__(self,index):
        return "x{0}".format(index)
class funkyback():
    def __reversed__(self):
        return 'backwards!'
for seq in lst,CustomSequence(),funkyback():
    print('\n{}:'.format(seq.__class__.__name__),end=" " )
    for item in reversed(seq):
        print(item,end=",")
print("\nEnd")

#Enumerator - method adds a counter to an iterable and returns the enumerate object.
for iii in  enumerate(lst):
    print(iii)
enum= enumerate(lst)
print(enum)
enum_to_list=list(enum)
print(enum_to_list)    