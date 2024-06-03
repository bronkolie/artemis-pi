import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pin number

PIN = 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
try:
    while True:
        GPIO.output(PIN, GPIO.HIGH)
        input("Press enter to disable...")
        GPIO.output(PIN, GPIO.LOW)
        input("Press enter to enable...")
except KeyboardInterrupt:
    print("\nInterrupted. Exiting...")
finally:
    GPIO.cleanup()