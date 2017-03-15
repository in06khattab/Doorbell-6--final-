This repo is a internet-connected doorbell featuring:
- 4 separate doorbell-buttons to ring
- separate doorbell-sounds per doorbell-button
- textmessage


Todo’s and Features of the internet-connected, intercom-doorbell:
-	Create and update this README
-	Create the default startup routine
-	Add several doorbell-sounds and modify the doorbell to any sound you want
-	Add Door-open detection
-	Add working connection to any mobile phone
-	Snapshot gets taken using the camera
-	Sending a text to any person of choice XXXXX
-	Sending a Tweet to any person of choice
-	Muting the indoors music XXXXX
-	Dimming the indoors light XXXXX 
-	Intercom with Sound XXXXX See “Intercom to any device at home”
-	Intercom with Sound&Image XXXXX See “Intercom to any device at home”

Doorbell
Started with the raspberrypi doorbell project, image and manual on this site and the github-source.
Used also this (https://www.raspberrypi.org/learning/push-button-stop-motion/worksheet/) and this (https://www.raspberrypi.org/learning/getting-started-with-picamera/0) webblogs.
The program to be run is a python script: LCD3.py or start.py

Create the default startup routine
Conform http://www.mikeslab.net/?p=176, I created a script and did “sudo /etc/init.d/doorbell.sh start”. Did not work. 
Added it to crontab with “@reboot /etc/init.d/doorbell.sh start” that did kick of the script, but no doorbell was started.
Added it to /.config/autoload 
[Desktop Entry]
Exec=”/etc/init.d/doorbell.sh start”
Type=Application
With no result
The crontab-log did show that the script did start. Just no response was shown at all.
Hardware Parts
- raspberry pi 1B, https://www.raspberrypi.org/products/model-b/, incl. 8GB microsd. €35
- recordingpart:
	- picam, https://www.raspberrypi.org/products/camera-module/ buy here for €7,96
	- microphone, just any usb mic. I used “TRIXES Black Mini Desk Top USB Microphone Speaker” available at amazon.com for 3.99 pounds.
- communicating to the person at the door:
	- monitor,
		via the first 26 gpio-connectors, 3,5" touchscreen for €26
		via the hdmi-port, 5" touchscreen 
	- speaker, "Mini Portable Speaker for the Raspberry Pi" bought at pi-supply.com €17,56
komt binnen 20 werkdagen, uiterlijk 11 october.
Altogether €86,50 +mic +buttons
Software
Camera
Started with https://www.raspberrypi.org/blog/internet-doorbell/. Then made these changes:
Made it pi3-bootable by “sudo apt-get update”, “sudo apt-get upgrade”;
Installing the software for the 3,5”screen
(optional) Install matchboardkeyboard from ozzmaker.com/virtual-keyboard-for-the-raspberry-pi
Copied and extracted LCD-show

For a complete manual: http://picamera.readthedocs.io/en/release-1.3/
For sample time-laps-projects: https://www.raspberrypi.org/blog/timelapse-tutorial-from-carrie-annes-geek-gurl-diaries/
Intercom to any device at home
Call via Ekiga.net
Sign up for an account at Ekiga.net: Your SIP address is: sip:timvansteenbergen@ekiga.net met wachwoord Poesa9876!
Install the Ekiga software on your device of choice. Might be your mobile, or your desktop
Install the Twinkle on the Pi: sudo apt-get install python-twinkle
Tweeting
Install tweepy in the Pi: sudo apt-get install python-tweepy
Get or create your own Twitter-account
Create an app on that Twitter-account
This will get you the customkey, customersecrets, accesskey and accesssecret that you need to enter into tweet.py
In command Tweet, change the start of variable ‘line’ to your own Twitter-account.

Streaming from the pi to Bambuser
Only works with a $35 monthly fee to Bambuser.
  - Bambuser API-key 3795bf3a4eb8b476c0c186288b432d41, see https://bambuser.com/api/keys
  - installation as by http://www.recantha.co.uk/blog/?p=4052
    - apt-get update
    - apt-get install ffmpeg
    - etc, but You do need a Premium-Bambuser-account, a free one won't let you do a live stream.

Raspberry-pi commands and hints&tips
Get the audio working
http://cagewebdev.com/raspberry-pi-getting-audio-working/
Installing the usb-mic
Plug in the mic in a usb-port
sudo apt-get install vim git-core python-dev python-pip bison libasound2-dev libportaudio-dev python-pyaudio –yes
sudo vim /etc/modprobe.d/alsa-base.conf
….pffffff
Adding an item to the menu
http://cagewebdev.com/raspberry-pi-adding-start-menu-items/
Switching between touchscreen and HDMI
On commandline give the command: HDMI-SYS-SHOW vs. LCD35-SYS-SHOW. Either one will reboot the pi.
Information about the OS
Command “cat /etc/os-release”
Information about the computer
Command “uname” gives the OSname.
With parameters like –o for type of OS. Currently ‘Jessie’. See man uname for other parametervalues.
Playing a sound
As well documented here, use omxplayer for mp3’s: 
“omxplayer example.mp3” if needed add “-o local” to get it to play over the headphones you plugged in at the headphone jack.
“omxplayer doorbell_lcd/Doorbell-6--final-/sounds/01_J_Attendais.mp3 -o local”

As sidetrack installed a Pi-Hole as a Networkwide Adblocker, see https://pi-hole.net. Installed on any pi with this command: 
curl –L https://install.pi-hole.net/ | bash
PI-Hole server settings
Static ip-address:  192.168.2.9/24
Gateway 192.168.2.254
Upstream DNS provider: OpenDNS (Can be changed to Google, OpenDNS, Level3, Norton, Comodo)
Thompson Router: 192.168.2.254