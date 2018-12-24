'''
Created on Dec 24, 2018

@author: ksinha
'''
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from future.backports.email import encoders

def sendmail(toaddr,msg):  
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("kaushal.opensource@gmail.com", "Accenture@123")  #(username,password)
    #message =msg    # "Hello Test From Python2"
    main_msg=MIMEMultipart()
    main_msg.attach(MIMEText(msg,'plain'))
    fname='TestPython.txt'
    attch=open(r'C:\Users\ksinha\eclipse-workspace\SamplePython\Email\TestPython.txt','rb')
#     p=MIMEBase('application','octet-stream')
#     p.set_payload((attch).read())

    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % fname)
    main_msg.attach(p)
    txt=main_msg.as_string()
    fromaddr="kaushal.opensource@gmail.com"
    s.sendmail(fromaddr, toaddr, txt)
    s.quit()

with open(r'C:\Users\ksinha\eclipse-workspace\SamplePython\Email\contact.csv','r') as file:
    reader = csv.reader(file)
    next(reader)
    for toaddr,msg in reader:
        print("sending mail to ",toaddr)
        sendmail(toaddr, msg)