#!/usr/bin/python
import urllib2
from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import RPi.GPIO as GPIO
import time
from time import gmtime, strftime
import os

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

while True:
    if not GPIO.input(14):  # button pressed
        lcd.clear()
        lcd.message("Ding Dong at\n")
        lcd.message(strftime("%d-%m-%Y %H:%M:%S"))
        os.system("sudo python send_email_fast.py")  # put a space within the quote after .py to insert an argument
        os.system("sudo python tweet.py")
        os.system("sudo python zapier_webhook.py")  # put a space within the quote after .py to insert an argument

        time.sleep(0.2)
