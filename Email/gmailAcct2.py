'''
Created on Dec 24, 2018

@author: ksinha
'''
import smtplib
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
#https://myaccount.google.com/lesssecureapps  --- MAKE UR GMAIL ALLOW TO USE THIS SERVICE
  
# Authentication 
s.login("kaushal.opensource@gmail.com", "Accenture@123")  #(username,password)
  
# message to be sent 
message = "Hello Test From Python2"
  
# sending the mail 
s.sendmail("kaushal.opensource@gmail.com", "kaushal.bksc@gmail.com", message)
#( 
  
# terminating the session 
s.quit() 