#!/usr/bin/python
import urllib2
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from gpiozero import Button
from Ringer import FamilyOrFriend, Salesman, Deliverer, HansOrGrietje
from RingerSingleButton import SingleButton

EMAIL = 'in06khattab@gmail.com; timvans@gmail.com'

b7red = Button(7)
# Set 4 doorbell-buttons connected to GPIO's 16, 18, 19 & 20, while 17 is connected to Ground
b21blue = Button(21)
b20yellow = Button(20)
b16green = Button(16)
b12white = Button(12)

# Initialize the LCD plate.  
try:
    lcd = Adafruit_CharLCDPlate()
    lcd.clear()
    lcdIsOperational = True
except:
    lcdIsOperational = False

if lcdIsOperational:  # Clear display and show greeting, pause 1 sec
    lcd.clear()
    lcd.backlight(lcd.ON)
    lcd.message("Welcome to your\ndoorbell")


def internet_on():


    """This function tests if there is a connection to the internet.
    Will return a boolean, true when connected, false if there is no connection."""
    try:
        urllib2.urlopen('http://www.google.com', timeout=10)
        return True
    except urllib2.URLError:
        pass
    return False


# lcd.clear()
if internet_on():
    print('Internet is up')
    # lcd.message("Internet is set\nup :)")
else:
    print('Internet is down')
    # lcd.message("No internet use\nDoorbell wifi")

while True:
    doorbell_pressed = False
    while not doorbell_pressed:
        if b21blue.is_pressed:
            ringer = FamilyOrFriend()
            doorbell_pressed = True
        if b20yellow.is_pressed:
            ringer = Salesman()
            doorbell_pressed = True
        if b16green.is_pressed:
            ringer = Deliverer()
            doorbell_pressed = True
        if b12white.is_pressed:
            ringer = HansOrGrietje()
            doorbell_pressed = True
        if b7red.is_pressed:
            ringer = SingleButton()
            doorbell_pressed = True
    if doorbell_pressed:
        ringer.respond()
