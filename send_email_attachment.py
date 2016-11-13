#!/usr/bin/env python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
from time import gmtime, strftime
import os
# from constants import _const

USERNAME = "doorbellding@gmail.com"
PASSWORD = "doorbell2"
MAILTO = "tim@tieka.nl"
MOSTRECENTSNAPSHOT = '/home/pi/camera/images/mostrecent.jpg'


def sendmail():
    print('Starting sendmail\n')
    msg = MIMEMultipart()
    text = "Hi, \n\nSomeone knocked on your door at " + strftime("%l:%M %p on %d-%m-%Y") + ".\n\nHave a great day!"
    msg['to'] = MAILTO
    msg['from'] = "doorbellding@gmail.com"
    msg['subject'] = "Ding Dong at " + strftime("%l:%M %p on %d-%m-%Y")

    msg.attach(MIMEText(text))
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(MOSTRECENTSNAPSHOT, "rb").read())
    Encoders.encode_base64(part)

    part.add_header('Content-Disposition', 'attachment; filename="photo.jpg"')

    msg.attach(part)
    print('Het bericht is:' + str(msg.as_string))
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo_or_helo_if_needed()
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, MAILTO, msg.as_string())
    print('\nVerzonden')
    server.quit()

