import StepperDriverLib_new as stepLib # imports variables and functions from StepperDriverLib script
import RPi.GPIO as GPIO
import time

step_delay = 2  # higher value = lower step speed
stepLib.setupStepperPins(pinA=7, pinB=6, pinC=12, pinD=24)


# stepLib.printPinSetup()
# print(f"coil A is set to pin {stepLib.coil_A_pin} within the library")  # we are able to access variables from other lib

# stepLib.moveStepper(100, delay=step_delay) # move stepper 100 steps

# time.sleep(1)

# stepLib.moveStepper(-200, delay=step_delay) # move stepper backwards 200 steps

# time.sleep(1)

# for i in range(50):
#     stepLib.moveStepper(2, delay=step_delay*3)  # move stepper 3 times slower, split up the total steps in smaller steps

stepLib.moveStepper(1000, delay=step_delay) # move stepper 100 steps

GPIO.cleanup()
print("finished")