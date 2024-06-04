import RPi.GPIO as GPIO
import time



PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
try:
    while True:
        GPIO.output(PIN, GPIO.LOW)
        input("Press enter to enable...")
        GPIO.output(PIN, GPIO.HIGH)
        input("Press enter to disable...")
    # while True:
    #     GPIO.output(PIN, GPIO.LOW)
    #     time.sleep(1/1000)
    #     GPIO.output(PIN, GPIO.HIGH)
    #     time.sleep(1/1000)

except KeyboardInterrupt:
    print("\nInterrupted. Exiting...")
finally:
    GPIO.cleanup()