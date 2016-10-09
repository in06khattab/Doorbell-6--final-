#!/usr/bin/python
import urllib2
from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  
lcd = Adafruit_CharLCDPlate()

# Clear display and show greeting, pause 1 sec
lcd.clear()
lcd.backlight(lcd.ON)
lcd.message("Welcome to your\ndoorbell")
sleep(1)


def internet_on():
    try:
        urllib2.urlopen('http://www.google.com',timeout=10)
        return True
    except urllib2.URLError: pass
    return False
        
lcd.clear()
if internet_on():
    lcd.message("Internet is set\nup :)")
else:
    lcd.message("No internet use\nDoorbell wifi")
