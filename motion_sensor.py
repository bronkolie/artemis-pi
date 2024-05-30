import RPi.GPIO as GPIO
import time




GPIO.setmode(GPIO.BCM)


# Set up the motion sensor GPIO pin
motion_sensor_pin = 23
GPIO.setup(motion_sensor_pin, GPIO.IN, GPIO.PUD_UP)

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

