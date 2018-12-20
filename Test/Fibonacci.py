'''
Created on Nov 30, 2018
LOOPS
@author: ksinha
'''

def fib2(n):
    a, b = 0, 1
    result=[]
    while b <n:
        result.append(b)
        a, b = b, a+b
    return result   
# CALLING FUNCTION

aa=fib2(5)
aa.append("No more Required")
print(aa)



# # FUNCTION DEFINATION
# def fib(n):
#     a, b = 0, 1
#     while b <n:
#         print(b,end=' ') #PRINT IN SAME LINE
#         a, b = b, a+b
# 
# # CALLING FUNCTION
# fib(5)

# print()
# print("LOOP TEST")    
# #FOR LOOP
# for n in range(1,10):
#     print("HAVE: ",n,": ",n%2)
#     if (n%2==0):
#         print(n)
#         
# # IF ELIF ELSE CONDITIONAL STATEMENT
# x = int(input("Please enter an integer: "))
# if x<0:
#     print("NEGATIVE")
# elif x==0:
#     print("ZERO")
# elif x==1:
#     print("UNIT VALUE")
# else:
#     print("SOMETHING ELSE")
# print(x)

