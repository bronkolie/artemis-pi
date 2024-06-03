import RPi.GPIO as GPIO
import time

INPUT_PIN = 5
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_PIN, GPIO.IN, GPIO.PUD_DOWN)

def main():
    while True:
        print(GPIO.input(INPUT_PIN))
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting...")
    finally:
        GPIO.cleanup()