from subprocess import call
from datetime import datetime
from time import sleep
import picamera
import send_email_attachment


class Ringer(object):
    # camera = picamera.PiCamera()

    # Set my picam

    def capture(self):
        datetimestamp = datetime.now().isoformat()
        self.camera.capture('/home/pi/camera/images/visitor%s.jpg' % datetimestamp)

    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (1024, 768)

    def __del__(self):
        self.camera.close()

    def respond(self):
        datetimestamp = datetime.now().isoformat()
        self.camera.capture('/home/pi/camera/images/visitor%s.jpg' % datetimestamp)
        self.camera.close()


class FamilyOrFriend(Ringer):
    def respond(self):
        super(FamilyOrFriend, self).respond()
        mp3sound = "/home/pi/doorbell/sounds/beep-01.mp3"
        call(["omxplayer",mp3sound, "-o", "local"])
# Todo1 make this work:        send_email_attachment
# Todo1 make this work:        send_email_attachment

class Salesman(Ringer):
    def respond(self):
        super(Salesman, self).respond()
        print("bugger off!!")
        sleep(1)


class Deliverer(Ringer):
    def respond(self):
        super(Deliverer, self).respond()
        mp3sound = "/home/pi/doorbell/sounds/beep-03.mp3"
        call(["omxplayer",mp3sound, "-o", "local"])


class HansOrGrietje(Ringer):
    def respond(self):
        super(HansOrGrietje, self).respond()
        mp3sound = "/home/pi/doorbell/sounds/beep-04.mp3"
        call(["omxplayer",mp3sound, "-o", "local"])
