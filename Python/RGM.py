#Knop activeert IR licht
#IR sensor activeert hovercraft

import RPi.GPIO as GPIO
import time, board, busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import threading

BUTTON_PIN = 4
IMPACT_SENSOR_PIN = 5
IR_LED_PIN = 17
ADC = True
IR_TRIGGER_VOLTAGE = 3
RELAY_PIN = 8
LED_PIN = 20
MOTION_SENSOR_ANALOG_PIN = 0
HOVERCRAFT_TIME = 3
ROCKET_TIME = 3


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(IR_LED_PIN, GPIO.IN)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.setup(IMPACT_SENSOR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)


def print_button():
    print("Waiting for button press...")
    start = time.time()

    while True:
        # Read the button state
        button_state = GPIO.input(BUTTON_PIN)
        if button_state:
            print(f"Button pressed after {(round(time.time() - start,3))}s")
            break
        time.sleep(0.025)



if ADC:
    # Create the I2C bus (I2C must be ENABLED on the Pi!!)
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the ADC object using the I2C bus
    ads = ADS.ADS1115(i2c)

    channels = []

    channels.append(AnalogIn(ads, ADS.P0))
    channels.append(AnalogIn(ads, ADS.P1))




def print_ir(length=0):
    print("Waiting for IR light...")
    start_time = time.time()
    while True:
        
        time.sleep(0.025)
        voltage = channels[0].voltage
        print(voltage)
        # if voltage > IR_TRIGGER_VOLTAGE:
        #     # print(voltage)
        #     print(f"IR detected after {round(time.time() - start_time, 3)}s")
        #     break


        if length != 0 and time.time() - start_time > length:
            return



def ir_led(low=True):
    if low:
        GPIO.output(IR_LED_PIN, GPIO.LOW)
    else:
        GPIO.output(IR_LED_PIN, GPIO.HIGH)

def is_ir_detected():
    return channels[MOTION_SENSOR_ANALOG_PIN].voltage > IR_TRIGGER_VOLTAGE
   
def check_ir():
    while True:
        if is_ir_detected():
            print("IR Detected")
            enable_hovercraft()
            return
        if stop_detecting:
            return
        time.sleep(0.025)
    
            
def enable_hovercraft():
    print("Activating hovercraft")
    GPIO.output(RELAY_PIN, GPIO.HIGH)
    time.sleep(HOVERCRAFT_TIME)
    print("Stopping hovercraft")
    GPIO.output(RELAY_PIN, GPIO.LOW)



def check_impact():
    keep_checking_impact = True
    def impact_detected_callback(channel):
        print("Impact detected!")
        start_rocket()
        GPIO.remove_event_detect(IMPACT_SENSOR_PIN)
        nonlocal keep_checking_impact
        keep_checking_impact  = False
        
    GPIO.add_event_detect(IMPACT_SENSOR_PIN, GPIO.RISING, callback=impact_detected_callback, bouncetime=500)
    while not stop_detecting and keep_checking_impact:
        time.sleep(0.1)


def start_rocket():
    print("Starting rocket...")
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(ROCKET_TIME)
    print("Stopping rocket...")
    GPIO.output(LED_PIN, GPIO.LOW)

def main():
    ir_detector = threading.Thread(target=check_ir)
    impact_detector = threading.Thread(target=check_impact)
    ir_detector.start()
    impact_detector.start()
    ir_detector.join()
    impact_detector.join()


if __name__ == "__main__":
    try:
        stop_detecting = False
        main()
    except KeyboardInterrupt:
        stop_detecting = True
        print("\nKeyboard interrupted. Exiting...")
    finally:
        GPIO.output(RELAY_PIN, GPIO.LOW)
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.cleanup()

