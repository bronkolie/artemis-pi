import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pin number

GPIO.setwarnings(False)
PIN = 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
try:
    GPIO.output(PIN, GPIO.HIGH)
    input("Enter to exit...")
except KeyboardInterrupt:
    print("Interrupted. Exiting...")
finally:
    GPIO.cleanup()