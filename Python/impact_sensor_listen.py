import RPi.GPIO as GPIO
import time




GPIO.setmode(GPIO.BCM)


# Set up the motion sensor GPIO pin
IMPACT_SENSOR_PIN = 5
GPIO.setup(IMPACT_SENSOR_PIN, GPIO.IN)




counter = 0
GPIO.setup(IMPACT_SENSOR_PIN, GPIO.IN)


def button_pressed_callback(channel):
    print("Motion detected!")
    time.sleep(1)


GPIO.add_event_detect(IMPACT_SENSOR_PIN, GPIO.RISING, callback=button_pressed_callback, bouncetime=500)

try:
    # Keep the script running
    print("Waiting for motion...")
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    # Clean up GPIO settings before exiting
    GPIO.cleanup()
    print("Exiting program")