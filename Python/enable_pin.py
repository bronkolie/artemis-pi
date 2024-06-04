import RPi.GPIO as GPIO




PIN = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
try:
    while True:
        GPIO.output(PIN, GPIO.LOW)
        input("Press enter to enable...")
        GPIO.output(PIN, GPIO.HIGH)
        input("Press enter to disable...")

except KeyboardInterrupt:
    print("\nInterrupted. Exiting...")
finally:
    GPIO.cleanup()