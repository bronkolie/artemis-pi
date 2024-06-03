"""https://tutorials-raspberrypi.com/how-to-control-a-stepper-motor-with-raspberry-pi-and-l293d-uln2003a/"""
import RPi.GPIO as GPIO
import time

coil_A_pin = 1 # pink
coil_B_pin = 2 # blue
coil_C_pin = 3 # orange
coil_D_pin = 4 # yellow
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
# adjust if different
Seq = [[1, 0, 0, 1],
       [1, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 1, 1]]
StepCount = len(Seq)
 


def setupStepperPins(pinA: int, pinB: int, pinC: int, pinD: int):
    global coil_A_pin, coil_B_pin, coil_C_pin, coil_D_pin
    coil_A_pin, coil_B_pin, coil_C_pin, coil_D_pin = pinA, pinB, pinC, pinD
    GPIO.setup([coil_A_pin, coil_B_pin, coil_C_pin, coil_D_pin], GPIO.OUT)
def printPinSetup():
    print(f"A pin: {coil_A_pin} ||  B pin: {coil_B_pin} || C pin: {coil_C_pin} || D pin: {coil_D_pin}")
 
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_pin, w1)
    GPIO.output(coil_B_pin, w2)
    GPIO.output(coil_C_pin, w3)
    GPIO.output(coil_D_pin, w4)

# steps = 5.625*(1/8) per step, 512 steps is 360°
def moveStepper(steps, delay=2):
    delay /= 1000
    if steps > 0:
        step_range = range(StepCount)
    else:
        step_range = range(StepCount-1, -1, -1)  # reversed

    for _ in range(abs(steps)):
        for j in step_range:
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)

# run this part if this script is our main/initial script (ran first).
if __name__ == '__main__':
    try:
        setupStepperPins(coil_A_pin, coil_B_pin, coil_C_pin, coil_D_pin)
        while True:
            delay = input("Time Delay (ms, default is 2)?")
            steps = input("How many step (negative is backwards)? ")
            moveStepper(int(steps), delay=int(delay))
    finally:
        GPIO.cleanup()
        print("\ncleaned up")
        
#         steps = input("How many steps forward? ")
#         forward(int(delay) / 1000.0, int(steps))
#         steps = input("How many steps backwards? ")
#         backwards(int(delay) / 1000.0, int(steps))