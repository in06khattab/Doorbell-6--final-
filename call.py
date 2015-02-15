import os
from time import sleep
import time
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
lcd = Adafruit_CharLCDPlate()
os.system("pkill -9 twinkle")
os.system("./call.sh")
print("hello")
while(1):
    if lcd.buttonPressed(lcd.SELECT):
       os.system("./call.sh")
       time.sleep(2)
       

        
    