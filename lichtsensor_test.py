import RPi.GPIO as GPIO
from gpiozero import LightSensor, Buzzer
import time
from StepperDriverLib import *

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

#input/output defineren
datapin = 20
outpin = [19, 13, 6, 5]
ledpin = 26
GPIO.setup(datapin, GPIO.IN)
GPIO.setup(outpin, GPIO.OUT)
GPIO.setup(ledpin, GPIO.OUT)

#zorgen dat lamp aan staat
GPIO.output(ledpin, GPIO.HIGH)

#kijken of de raket er is en dan de motor uitzetten
# try:
#     while True:
#         print("a")
#         moveStepper(1, delay=2)
#         print("b")
#         if GPIO.input(datapin) == 0:
#             print("c")
#             time.sleep(5)
#             print("d")
#             GPIO.output(outpin, GPIO.LOW)
#             print("e")
#             break
#         print("f")
#     print("g")
# except:
#     print("z")


while True:
    forward(steps=100, delay=2)
    print("a")

# finally:
    # GPIO.cleanup()