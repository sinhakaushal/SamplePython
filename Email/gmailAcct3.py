'''
Created on Dec 24, 2018
https://www.tutorialspoint.com/python/python_sending_email.htm
@author: ksinha
'''
#!/usr/bin/python

import smtplib
import base64

filename = r'C:\Users\ksinha\eclipse-workspace\SamplePython\Email\TestPython.txt'

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

sender = 'kaushal.opensource@gmail.com'
reciever = 'kaushal.bksc@gmail.com'

marker = "AUNIQUEMARKER"

body ="""
This is a test email to send an attachement.
"""
# Define the main headers.
part1 = """From: From Person <me@fromdomain.net>
To: To Person <amrood.admin@gmail.com>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)

# Define the attachment section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2 + part3

try:
#     smtpObj = smtplib.SMTP('kaushal.opensource@gmail.com','Accenture@123')
#     smtpObj.starttls()
#     smtpObj.sendmail(sender, reciever, message)
    smtpObj=smtplib.SMTP('smtp.gmail.com',587)
    smtpObj.starttls()
    smtpObj.login('kaushal.opensource@gmail.com', 'Accenture@123')
    smtpObj.sendmail(sender, reciever, message)
    print("Successfully sent email")
except Exception:
    print ("Error: unable to send email")