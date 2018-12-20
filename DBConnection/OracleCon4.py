'''
Created on Dec 19, 2018

@author: ksinha
'''
import cx_Oracle
connection = cx_Oracle.connect('IDESK_DATA','IDESK_DATA','ny-rac-nprdee01.na.rtdom.net/prsmqa2_d')
cursor = connection.cursor()
cursor.execute("Select * from AUTO_CAMP_PRISMA_BUY_DETAIL order by 1")
db_dict={}
for i in cursor.fetchmany(numRows=3):
    print(len(i))
    db_dict[i[0:3]]=i[3:]
    #print("DB_DICT:",len(db_dict))
    print(db_dict)
cursor.close()    
connection.close()

print(db_dict)
print("TOTAL DB-DICT:",len(db_dict))
dict2=db_dict
for i in db_dict:
    print(i,"::",db_dict[i])
#print(":",dict2)    

#cursor.fetchaone() -This uses the fetchone() method to return just a single row as a tuple. When called multiple time, consecutive rows are returned:
#cursor.fetchall() - This uses the fetchall() method to return all rows. The output is a list (Python's name for an array) of tuples. Each tuple contains the data for one row.
#cursor.fetchmany(numRows=3) - The fetchmany() method returns a list of tuples. Here the numRows parameter specifices that three rows should be returned.
