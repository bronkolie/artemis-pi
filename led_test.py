import RPi.GPIO as GPIO
from gpiozero import LightSensor, Buzzer
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

datapin = 20
ledpin = 26
GPIO.setup(ledpin, GPIO.OUT)
GPIO.setup(datapin, GPIO.IN)

while True:
    GPIO.output(ledpin, GPIO.LOW)
    print(GPIO.input(datapin))
    time.sleep(0.5)