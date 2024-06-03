#Knop activeert IR licht
#IR sensor activeert hovercraft

import RPi.GPIO as GPIO
import time, board, busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

BUTTON_PIN = 4
IMPACT_SENSOR_PIN = 5
IR_LED_PIN = 17
ADC = False
IR_TRIGGER_VOLTAGE = 3
RELAY_PIN = 8
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(IR_LED_PIN, GPIO.IN)



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

def amogus():
    print("Aamogus")

def ir_led(low=True):
    if low:
        GPIO.output(IR_LED_PIN, GPIO.LOW)
    else:
        GPIO.output(IR_LED_PIN, GPIO.HIGH)

def impact_sensor_listen():
    # Set up the motion sensor GPIO pin

    GPIO.setup(IMPACT_SENSOR_PIN, GPIO.IN)
    GPIO.setup(IMPACT_SENSOR_PIN, GPIO.IN)

    def button_pressed_callback(channel):
        print("Motion detected!")
        amogus()


    GPIO.add_event_detect(IMPACT_SENSOR_PIN, GPIO.RISING, callback=button_pressed_callback, bouncetime=500)



def main():
    impact_sensor_listen()
    input("Press enter to exit...\n")
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard interrupted. Exiting...")
    finally:
        GPIO.cleanup()

