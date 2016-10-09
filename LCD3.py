#!/usr/bin/python
import urllib2
from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import RPi.GPIO as GPIO
import time
from time import gmtime, strftime
import os
import subprocess

EMAIL = 'in06khattab@gmail.com'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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
    if not GPIO.input(7):  # button pressed
        print("button pressed")
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

    # Local video
    if lcd.buttonPressed(lcd.LEFT):
        proc = subprocess.Popen([
            "raspivid -t 0 -b 2000000 -n -o - | gst-launch-1.0 -e -vvvv fdsrc ! h264parse ! flvmux ! rtmpsink location=rtmp://localhost/rtmp/live"],
            shell=True)
        print("aa")
        (out, err) = proc.communicate()
        print("program output:", out)

    if lcd.buttonPressed(lcd.RIGHT):
        print("aa")
        proc = subprocess.Popen(["pkill gst-launch-1.0; pkill raspivid"], shell=True)
        (out, err) = proc.communicate()
        print("program output:", out)
        # os.system("raspivid -o - -t 0 -w 1270 -h 720 -fps 25 -b 600000 -g 50 | ./ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/DoorBellDing.rpt9-wuhk-ctju-dgxw")

    if lcd.buttonPressed(lcd.DOWN):
        lcd.clear()

        proc = subprocess.Popen(["/sbin/ifconfig wlan0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'"],
                                stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        # print "program output:", out

        lcd.message(out)
