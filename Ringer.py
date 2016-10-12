from subprocess import call
from datetime import datetime
from time import sleep
import picamera
import os
from send_email_attachment import sendmail
from tweet import tweet
from shutil import copyfile


class Ringer(object):

    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1024, 768)

    def __del__(self):
        self.camera.close()

    def respond(self):
        datetimestamp = datetime.now().isoformat()
        newfile = '/home/pi/camera/images/visitor%s.jpg' % datetimestamp
        mostrecentfile = '/home/pi/camera/images/mostrecent.jpg'
        self.camera.capture(newfile)
        self.camera.close()
        # os.remove(mostrecentfile)
        copyfile(newfile, mostrecentfile)


class FamilyOrFriend(Ringer):
    def respond(self):
        super(FamilyOrFriend, self).respond()
        mp3sound = "sounds/beep-01.mp3"
        call(["omxplayer",mp3sound, "-o", "local"])
# Todo2 make this work, Ekiga.net and Twinkle
#         os.system("./call.sh")
        sendmail()  # Works fine.
        tweet()  # Works fine.

class Salesman(Ringer):
    def respond(self):
        super(Salesman, self).respond()
        print("bugger off!!")
        sleep(1)


class Deliverer(Ringer):
    def respond(self):
        super(Deliverer, self).respond()
        mp3sound = "sounds/beep-03.mp3"
        call(["omxplayer",mp3sound, "-o", "local"])


class HansOrGrietje(Ringer):
    def respond(self):
        super(HansOrGrietje, self).respond()
        mp3sound = "sounds/knibbelknabbelknuisje.amr"
        call(["omxplayer",mp3sound, "-o", "local"])
