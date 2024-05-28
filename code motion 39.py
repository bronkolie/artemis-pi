import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set up the motion sensor GPIO pin
motion_sensor_pin = 6
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
