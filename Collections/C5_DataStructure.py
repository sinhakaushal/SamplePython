#LIST
from _collections import deque

ls = []
ls.append(21)
ls.append(22)
ls2=[11,12,13]
print("list 1:", len(ls)," : ",ls)
print("list 2:", len(ls2)," : ",ls2)
ls.extend(ls2)
print(ls)
ls.insert(2,14)
print(ls)
ls.remove(14)
print(ls)
print(ls.pop(2))
ls.sort(key=None, reverse=False)
print(ls)
ls.reverse()
print(ls)

# LIST as STACK
print("LIST as STACK")
list_stack=[12,5,19,89]
print(list_stack)
list_stack.append(2018)
list_stack.append(2019)
print(list_stack)
print(list_stack.pop())
print(list_stack)
print(list_stack.pop())
print(list_stack)

#LIST as QUEUE
print("LIST as QUEUE")
guest=["Amit","Piyali","Sonali"]
print(guest)
guest_q=deque(guest)
print(guest_q)
guest_q.append("Kaushal")
guest_q.append("Ratnesh")
print(guest_q)
print(guest_q.popleft())
print(guest_q.popleft())
print(guest_q)

# TUPLE : List with number and SQUARE
sq=[(x, x**2,x**3) for x in range(2,10)]
print(sq)
print(sq.pop(2)[0:2])
l=[w.strip() for w in guest]
print(l)

#SET : List without duplicates
name= ["Amit","Anish","Ratnesh","Rahul","Amit","Rahul"]
print("NAME LIST:",name)
print("NAME SET:",set(name))

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a
#set(['a', 'r', 'b', 'c', 'd'])
print(a - b)                              # letters in a but not in b
#set(['r', 'd', 'b'])
print(a | b)                              # letters in either a or b
#set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
print(a & b)                              # letters in both a and b
#set(['a', 'c'])
print(a ^ b)                              # letters in a or b but not both
#set(['r', 'd', 'b', 'm', 'z', 'l'])



# DICTIONAY: KEY VALUE: - KEY are immutable and values are mutable
sq={x: x**2 for x in range(1,10)}
print(sq[7])
cube={x: x**3 for x in range(1,10)}
print(cube)

#ENMURATION 
for  i , v in enumerate(guest):
    print(i,":",v)
 
for  iguest in reversed(guest):
    print(iguest)
for  i , v in enumerate(sorted(guest)):
    print(i,":",v)    