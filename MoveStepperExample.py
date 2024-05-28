from StepperDriverLib import *  # imports variables and functions from StepperDriverLib script, see pin setup in script

printPinSetup()
print(coil_A_pin)  # we are able to access variables from other lib

moveStepper(100) # move stepper 100 steps

time.sleep(1)  # time library already imported within StepperDriverLib library, thus we can reuse

moveStepper(-200) # move stepper backwards 200 steps

time.sleep(1)

moveStepper(100, delay=4)  # move stepper with a dealy of 4 ms between each step, default = 2ms

print("finished")