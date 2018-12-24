'''
Created on Dec 24, 2018

@author: ksinha
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage  
from email.mime.base import MIMEBase
import base64
msg=MIMEMultipart()
fromaddress='kaushal.openesource@gmail.com'
toaddress='kaushal.bksc@gmail.com'
msg['From']=fromaddress
msg['To']=toaddress
msg['Subject']='PYTHON TEST Image Attachment'
body='Hello Mail for tetsing the Python'
msg.attach(MIMEText(body,'plain'))

# Add Image as Attachment to mail
fp = open(r'C:\Users\ksinha\Pictures\1983copy.jpg', 'rb') #Using raw prefix and single quotes (i.e. '...')
img = MIMEImage(fp.read())
fp.close()
msg.attach(img)

# Add File as Attachment to mail
# fp1 = open(r'C:\Users\ksinha\Documents\Sumit_Sahu_CV_2018.docx', 'rb') #Using raw prefix and single quotes (i.e. '...')
# # txtfile = MIMEBase(fp1.read(),None)
# # fp1.close()
# # msg.attach(txtfile)
# txtfile = MIMEBase('text', 'docx')
# txtfile.set_payload(fp1.read())
# fp1.close()
# # Encode the payload using Base64
# #encoders.encode_base64(txtfile)
# msg.attach(txtfile)

# Read a file and encode it into base64 format
# fo = open(r'C:\Users\ksinha\eclipse-workspace\SamplePython\Email\TestPython.txt', "rb")
# filecontent = fo.read()
# encodedcontent = base64.b64encode(filecontent)  # base64
# msg=encodedcontent


#Sending Mail STEP
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('kaushal.opensource@gmail.com', 'Accenture@123')
text=msg.as_string()
server.sendmail(fromaddress,toaddress,text)
print("Mail Sent")
server.quit()