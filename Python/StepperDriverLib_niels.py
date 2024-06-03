"""https://tutorials-raspberrypi.com/how-to-control-a-stepper-motor-with-raspberry-pi-and-l293d-uln2003a/"""
coil_A_pin = 19 # pink
coil_B_pin = 13 # blue
coil_C_pin = 6 # orange
coil_D_pin = 5 # yellow


import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

 
# adjust if different
StepCount = 8
Seq = list(range(0, StepCount))
Seq[0] = [0,1,0,0]
Seq[1] = [0,1,0,1]
Seq[2] = [0,0,0,1]
Seq[3] = [1,0,0,1]
Seq[4] = [1,0,0,0]
Seq[5] = [1,0,1,0]
Seq[6] = [0,0,1,0]
Seq[7] = [0,1,1,0]
 
GPIO.setup(coil_A_pin, GPIO.OUT)
GPIO.setup(coil_C_pin, GPIO.OUT)
GPIO.setup(coil_B_pin, GPIO.OUT)
GPIO.setup(coil_D_pin, GPIO.OUT)

def printPinSetup():
    print(f"A pin: {coil_A_pin} || C pin: {coil_C_pin} || B pin: {coil_B_pin} || D pin: {coil_D_pin}")

 
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_pin, w1)
    GPIO.output(coil_C_pin, w2)
    GPIO.output(coil_B_pin, w3)
    GPIO.output(coil_D_pin, w4)
    
def moveStepper(steps, delay=2):
    delay /= 1000
    if steps > 0:
        forward(delay, steps)
    else:
        backwards(delay, -steps)
 
def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
 
def backwards(delay, steps):
    for i in range(steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
 
if __name__ == '__main__':
    while True:
        delay = input("Time Delay (ms, default is 1)?")
        steps = input("How many step (negative is backwards)? ")
        moveStepper(int(steps))
        
#         steps = input("How many steps forward? ")
#         forward(int(delay) / 1000.0, int(steps))
#         steps = input("How many steps backwards? ")
#         backwards(int(delay) / 1000.0, int(steps))