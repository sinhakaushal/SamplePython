'''
Created on Dec 19, 2018

@author: ksinha
Improve Query Performance
This section demonstrates a way to improve query performance by increasing the number of rows returned in each batch from Oracle to the Python program. 
TAKEN FROM: https://www.oracle.com/technetwork/articles/dsl/python-091105.html

2.Using Bind Variables
'''
import cx_Oracle
import time
connection = cx_Oracle.connect('IDESK_DATA','IDESK_DATA','ny-rac-nprdee01.na.rtdom.net/prsmqa2_d')
start=time.time()
cursor = connection.cursor()
cursor.arraysize=20000 #this is being used to set the timing.The default arraysize used by cx_Oracle is 50. There is a time/space tradeoff for increasing the arraysize. Larger arraysizes will require more memory in Python for buffering the records.
cursor.execute("Select * from all_tables order by 1")
res=cursor.fetchall()
elasped=(time.time()-start)
print(elasped,"second")
cursor.close()
connection.close()