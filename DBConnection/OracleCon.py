'''
Created on Nov 29, 2018

@author: ksinha
'''
import cx_Oracle
ls_imp=[]
ls_do=[]
connection = cx_Oracle.connect('BI_DATA','BI_DATA','ny-rac-nprdee01.na.rtdom.net/DEVCINY_D')
print(type(connection))
cursor = connection.cursor()
print(type(cursor))
cursor.execute("Select ID,NAME from BD_SOURCE")
dict_store={}
for column_1, column_2 in cursor.fetchall():
        ls_imp.append(column_1)
        ls_imp.append(column_2)
        
        ls_do.append((column_1,column_2))
        
        dict_store[column_1]=column_2
        print (column_1, "\t", column_2)
print(ls_imp)
print(ls_do)
print("+++++++++++++++++++++++++++++++++++++++")
print("DB Dict",dict_store)

cursor.execute("Select * from BD_SOURCE")
for column_1 in cursor.fetchall():
        print (column_1)
cursor.close()
connection.close()
# print('Test')
# print(cx_Oracle.clientversion())