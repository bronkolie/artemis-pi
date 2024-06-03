import RPi.GPIO as GPIO
import time

IRLED_PIN =
LED_PIN =
BUTTON_PIN =

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)

while True:
    if GPIO.input(BUTTON_PIN) == 1:
        GPIO.output(LED_PIN, GPIO.HIGH)
        GPIO.output(IRLED_PIN, GPIO.HIGH)
        time.sleep (5)
        break
         