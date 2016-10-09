#!/usr/bin/python
import urllib2
from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import RPi.GPIO as GPIO
import time
from time import gmtime, strftime
import os

EMAIL = 'in06khattab@gmail.com'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize the LCD plate.  
lcd = Adafruit_CharLCDPlate()

# Clear display and show greeting, pause 1 sec
lcd.clear()
lcd.backlight(lcd.ON)
lcd.message("Welcome to your\ndoorbell")
sleep(1)


def internet_on():
    try:
        urllib2.urlopen('http://www.google.com', timeout=10)
        return True
    except urllib2.URLError:
        pass
    return False


lcd.clear()
if internet_on():
    lcd.message("Internet is set\nup :)")
else:
    lcd.message("No internet use\nDoorbell wifi")

os.system("./call.sh")
while True:
    if lcd.buttonPressed(lcd.SELECT):  # button pressed
        time1 = strftime("%l:%M %p on %d-%m-%Y")
        message = "Ding Dong at " + strftime("%l:%M %p on %d-%m-%Y")
        time2 = strftime(" %l:%M %p")

        lcd.clear()
        lcd.message("Ding Dong at\n")
        lcd.message(strftime("%d-%m-%Y %H:%M:%S"))
        os.system("./call.sh")
        os.system("sudo python camera.py")
        # os.system("sudo python send_email_fast.py") #put a space within the quote after .py to insert an argument
        os.system("sudo python send_email_attachment.py")

        os.system(
            "sudo python zapier_webhook.py" + time2)  # put a space within the quote after .py to insert an argument
        os.system('sudo echo ' + message + ' | sendxmpp -v -t ' + EMAIL)  # send hangouts message
        os.system("sudo python tweet.py ")

        time.sleep(0.2)
