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
liedje = [0.5, 0.5, 0.4, 0.3, 0.9, 0.6, 0.7, 0.8, 0.9, 1.0]

#defineren wat het afspelen van het liedje is
def afspelen(fragment):
    GPIO.output(buzzerpin, GPIO.HIGH)
    time.sleep(fragment)
    GPIO.output(buzzerpin, GPIO.LOW)

#als erg geen licht gezien word wacht het even en dan speelt het het liedje af
while True:
    if GPIO.input(datapin) == 0:
        time.sleep(5)
        for fragment in liedje:
            afspelen(fragment)
