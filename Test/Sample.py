'''
Created on Nov 28, 2018

@author: ksinha
'''
import sys
print("Hello World")
try:
    file=open("TestPython.txt", "r")
except IOError:
    print("There was an error reading file")
    sys.exit()
file_text=file.read()
print(file_text)
file.close()