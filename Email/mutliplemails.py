'''
Created on Dec 24, 2018

@author: ksinha
'''
import smtplib
import csv
def sendmail(toaddr,msg):  
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587)
      
    # start TLS for security 
    s.starttls()
    #https://myaccount.google.com/lesssecureapps  --- MAKE UR GMAIL ALLOW TO USE THIS SERVICE
      
    # Authentication 
    s.login("kaushal.opensource@gmail.com", "Accenture@123")  #(username,password)
      
    # message to be sent 
    message =msg    # "Hello Test From Python2"
      
    # sending the mail 
    s.sendmail("KAUSHAL OPENSOURCE", toaddr, message)
    #( 
      
    # terminating the session 
    s.quit()


with open(r'C:\Users\ksinha\eclipse-workspace\SamplePython\Email\contact.csv','r') as file:
    reader = csv.reader(file)
    next(reader)
    for toaddr,msg in reader:
        print("sending mail to ",toaddr)
        sendmail(toaddr, msg)