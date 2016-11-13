from subprocess import call
from datetime import datetime
from time import sleep
import picamera
import os
from send_email_attachment import sendmail
from tweet import tweet
from shutil import copyfile
# from constants import _const


class Ringer(object):

    def __init__(self):
        try:
            self.camera = picamera.PiCamera()
            self.camera.resolution = (1024, 768)
        except:
            print('Something went horribly wrong. I lost my camera and can''t start it again without rebooting. So I will now reboot within 5 seconds.')
            sleep(5)
            # os.system('sudo shutdown -r now')

    def __del__(self):
        self.camera.close()

    def respond(self):
        datetimestamp = datetime.now().isoformat()
        newfile = '/home/pi/camera/images/visitor%s.jpg' % datetimestamp
        self.camera.capture(newfile)
        self.camera.close()
        # and copy the new image to the most recent snapshot to show on our inhouse-answering-devices
        MOSTRECENTSNAPSHOT = '/home/pi/camera/images/mostrecent.jpg'
        copyfile(newfile, MOSTRECENTSNAPSHOT)


class FamilyOrFriend(Ringer):
    def respond(self):
        super(FamilyOrFriend, self).respond() # Works fine
        mp3sound = "sounds/beep-01.mp3" # Works fine
        call(["omxplayer",mp3sound, "-o", "local"]) # Works fine
        sendmail()  # Works fine.
        tweet()  # Works fine.
# Todo2 make this work, Ekiga.net (and Twinkle) and the phone-app of linphone
        os.system("./call.sh") # does not work. Fails to connect to the phone


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