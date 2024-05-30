import RPi.GPIO as GPIO
import time

BUTTON_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)

def print_button():
    start = time.time()
    try:
        while True:
            # Read the button state
            button_state = GPIO.input(BUTTON_PIN)
            if button_state:
                print(f"Button pressed after {(round(time.time() - start,3))}s")
                break
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Exiting program")

    finally:
        GPIO.cleanup()