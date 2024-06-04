import RPi.GPIO as GPIO
from time import sleep


bpm = 150
beat = 60/bpm
PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

def switch():
    if GPIO.input(PIN):
        GPIO.output(PIN, GPIO.LOW)
    else:
        GPIO.output(PIN, GPIO.HIGH)

def note(length):
    switch()
    sleep(length*beat)
def pause(length):
    sleep(length*beat)
try:
    sleep(beat)
    note(1)
    note(1/3)
    note(1/3)
    note(1/3)
    note(1)
    note(1)
    pause(1)
    note(1)
    note(1)



except KeyboardInterrupt:
    print("\nInterrupted. Exiting...")
finally:
    GPIO.cleanup()