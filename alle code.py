import RPi.GPIO as GPIO
import time




IRLED_PIN =
LED_PIN =
BUTTON_PIN =




GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(IRLED_PIN, GPIO.OUT)


while True:
   if GPIO.input(BUTTON_PIN) == 1:
       GPIO.output(LED_PIN, GPIO.HIGH)
       GPIO.output(IRLED_PIN, GPIO.HIGH)
       time.sleep (5)
       GPIO.output(IRLED_PIN, GPIO.LOW)
       break






# Set up the motion sensor GPIO pin
motion_sensor_pin = 23
GPIO.setup(motion_sensor_pin, GPIO.IN)

try:
    while True:
        if GPIO.input(motion_sensor_pin) == 0:
            print("Motion detected!")
        else:
            print("No motion detected")
        time.sleep(0.5)  # Adjust the sleep time as needed
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()

import RPi.GPIO as GPIO
from gpiozero import LightSensor, Buzzer
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#input en output defineren
datapin = 20
buzzerpin = 12
ledpin = 26
GPIO.setup(ledpin, GPIO.OUT)
GPIO.setup(buzzerpin, GPIO.OUT)
GPIO.setup(datapin, GPIO.IN)


#lijst van wachttijden voor de buzzer
buzzen = [0.5] * 10


#defineren wat het afspelen van de buzzer is
def afspelen(fragment):
   GPIO.output(buzzerpin, GPIO.HIGH)
   time.sleep(fragment)
   GPIO.output(buzzerpin, GPIO.LOW)
   time.sleep(fragment)


#als erg geen licht gezien word wacht het even en dan gaat de buzzer buzzen
while True:
   if GPIO.input(datapin) == 0:
       time.sleep(5)
       for fragment in buzzen:
           afspelen(fragment)

