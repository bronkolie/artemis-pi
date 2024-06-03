import RPi.GPIO as GPIO
import time, board, busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import threading
import configparser

config = configparser.ConfigParser(inline_comment_prefixes="#")
config.read('rgm.conf')




BUTTON_PIN = int(config['digital_pins']['button'])
IMPACT_SENSOR_PIN = int(config['digital_pins']['impact_sensor'])
IR_LED_PIN = int(config['digital_pins']['ir_led'])
RELAY_PIN = int(config['digital_pins']['relay'])
LED_PIN = int(config['digital_pins']['led'])
SDA_PIN = int(config['digital_pins']['sda'])
SCL_PIN = int(config['digital_pins']['scl'])


HOVERCRAFT_TIME = float(config['times']['hovercraft'])
MIN_ROCKET_TIME = float(config['times']['min_rocket'])


IR_TRIGGER_VOLTAGE = float(config['voltages']['ir_trigger_voltage'])
LIGHT_TRIGGER_VOLTAGE = float(config['voltages']['light_trigger_voltage'])

IR_SENSOR_ANALOG_PIN = int(config['analog_pins']['ir_sensor'])
LIGHT_SENSOR_ANALOG_PIN = int(config['analog_pins']['light_sensor'])


ADC = True

if SDA_PIN != 2 or SCL_PIN != 3:
    raise Exception("The ADC was wired incorrectly.\nSDA must be connected to GPIO pin 2 and SCL must be connected to GPIO pin 3")


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
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
    channels.append(AnalogIn(ads, ADS.P2))
    channels.append(AnalogIn(ads, ADS.P3))




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
    return channels[IR_SENSOR_ANALOG_PIN].voltage > IR_TRIGGER_VOLTAGE

def is_light_detected():
    return channels[LIGHT_SENSOR_ANALOG_PIN].voltage < LIGHT_TRIGGER_VOLTAGE

   
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

def stop_rocket():
    print("Stopping rocket...")
    GPIO.output(LED_PIN, GPIO.LOW)

def check_light():
    while True:
        if is_light_detected():
            print("Light Detected!")
            stop_rocket()
            return
        if stop_detecting:
            return
        time.sleep(0.025)
    

def main():
    ir_detector = threading.Thread(target=check_ir)
    impact_detector = threading.Thread(target=check_impact)
    light_detector = threading.Thread(target=check_light)
    ir_detector.start()
    impact_detector.start()
    impact_detector.join()
    time.sleep(MIN_ROCKET_TIME)
    light_detector.start()
    light_detector.join()
    ir_detector.join()


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

