import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pin number
GPIO.setmode(GPIO.BCM)
PWM_PIN = 17

# Setup PWM pin
GPIO.setup(PWM_PIN, GPIO.IN)

try:
    while True:
        # Read the PWM duty cycle
        duty_cycle = GPIO.input(PWM_PIN)
        print("PWM Duty Cycle:", duty_cycle)
        time.sleep(0.5)  # Wait for a short time before reading again

except KeyboardInterrupt:
    # Clean up GPIO on Ctrl+C exit
    GPIO.cleanup()