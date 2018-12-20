'''
Created on Dec 19, 2018

@author: ksinha
'''
import sys
print("Hello World")
try:
    file=open("abc.txt", "r")
except IOError:
    print("There was an error reading file")
    sys.exit()
file_text=file.read()
print(file_text)
file.close()
try:
    file2=open("abc.txt", "a")
except IOError:
    print("There was an error reading file")
    sys.exit()
file2.write("New Line appended"'\n')
#print(file2.read())
file2.close()
