'''
Created on Dec 13, 2018

@author: ksinha
'''
import pyodbc

cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=NY-MSSQL-03\PRSMQA2;'
                      'Database=DMD;'
                      'uid=etl_user;pwd=W3lcom311')

cursor = cnxn.cursor()
cursor.execute('Select * from DMD.dbo.BIReport')

for i,row in i,cursor:
    
    print(row)