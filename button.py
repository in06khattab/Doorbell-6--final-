import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



while True:
    if GPIO.input(7) == False: #button pressed
        print('Button Pressed')
        time.sleep(5)