#!/usr/bin/python

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  
lcd = Adafruit_CharLCDPlate()

# Clear display and show greeting, pause 1 sec
lcd.clear()
lcd.backlight(lcd.ON)
lcd.message("Adafruit RGB LCD\nPlate w/Keypad!")
sleep(1)
