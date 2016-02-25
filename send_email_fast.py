#!/usr/bin/env python
import smtplib
from email.mime.text import MIMEText
from time import gmtime, strftime
 
USERNAME = "doorbellding@gmail.com"
PASSWORD = "doorbell2"
MAILTO  = "in06khattab@gmail.com"

msg = MIMEText("Hi, \n\nSomeone knocked on your door at "+strftime("%l:%M %p on %d-%m-%Y")+".\n\nHave a great day!")
msg['to'] = MAILTO
msg['from'] = "doorbellding@gmail.com"
msg['subject'] = "Ding Dong at "+strftime("%l:%M %p on %d-%m-%Y")

 
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo_or_helo_if_needed()
server.starttls()
server.ehlo_or_helo_if_needed()
server.login(USERNAME,PASSWORD)
server.sendmail(USERNAME, MAILTO, msg.as_string())
server.quit()
