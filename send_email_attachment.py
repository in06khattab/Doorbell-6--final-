#!/usr/bin/env python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
from time import gmtime, strftime
import os
 
USERNAME = "doorbellding@gmail.com"
PASSWORD = "doorbell2"
MAILTO="in06khattab@gmail.com"

def sendMail():
   
    msg = MIMEMultipart()
    text = "Hi, \n\nSomeone knocked on your door at "+strftime("%l:%M %p on %d-%m-%Y")+".\n\nHave a great day!"
    msg['to'] = MAILTO
    msg['from'] = "doorbellding@gmail.com"
    msg['subject'] = "Ding Dong at "+strftime("%l:%M %p on %d-%m-%Y")

 
    
    msg.attach( MIMEText(text) )
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("image.jpg", "rb").read())
    Encoders.encode_base64(part)

    part.add_header('Content-Disposition', 'attachment; filename="photo.jpg"')

    msg.attach(part)


    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login(USERNAME,PASSWORD)
    server.sendmail(USERNAME, MAILTO, msg.as_string())
    server.quit()
 
 
sendMail()
