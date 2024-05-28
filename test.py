import RPi.GPIO as GPIO           # import RPi.GPIO module  
from time import sleep


GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD  
GPIO.setup(6, GPIO.OUT) # set a port/pin as an output   
while True:
    GPIO.output(6, 1)       # set port/pin value to 1/GPIO.HIGH/True  
    GPIO.output(6, 0)       # set port/pin value to 0/GPIO.LOW/False  
    sleep(0.002)