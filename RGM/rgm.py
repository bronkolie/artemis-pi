import RPi.GPIO as GPIO
import time, board, busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import threading
import configparser
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

config = configparser.ConfigParser(inline_comment_prefixes="#")
config.read('rgm.conf')




BUTTON_PIN = int(config['digital_pins']['button'])
IMPACT_SENSOR_PIN = int(config['digital_pins']['impact_sensor'])
IR_LED_PIN = int(config['digital_pins']['ir_led'])
RELAY_PIN = int(config['digital_pins']['relay'])
ROCKET_PIN = int(config['digital_pins']['rocket'])
SDA_PIN = int(config['digital_pins']['sda'])
SCL_PIN = int(config['digital_pins']['scl'])
LED_PIN = int(config['digital_pins']['led'])
BUZZER_PIN = int(config['digital_pins']['buzzer'])


HOVERCRAFT_TIME = float(config['times']['hovercraft'])
MIN_ROCKET_TIME = float(config['times']['min_rocket'])

LIGHT_SENSOR_SURE = float(config['misc']['light_sensor_sure'])


IR_TRIGGER_VOLTAGE = float(config['trigger_voltages']['ir_sensor'])
LIGHT_TRIGGER_VOLTAGE = float(config['trigger_voltages']['light_sensor'])

IR_SENSOR_ANALOG_PIN = int(config['analog_pins']['ir_sensor'])
LIGHT_SENSOR_ANALOG_PIN = int(config['analog_pins']['light_sensor'])


if HOVERCRAFT_TIME % 1 == 0:
    HOVERCRAFT_TIME = int(HOVERCRAFT_TIME)

class WrongWiringException(Exception):
    def __init__(self, message="The ADC was wired incorrectly.\nSDA must be connected to GPIO pin 2 and SCL must be connected to GPIO pin 3"):
        self.message = message
        super().__init__(self.message)

if SDA_PIN != 2 or SCL_PIN != 3:
    raise WrongWiringException()

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
GPIO.setmode(GPIO.BCM)
# GPIO.setup(BUTTON_PIN, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(IR_LED_PIN, GPIO.IN)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.setup(IMPACT_SENSOR_PIN, GPIO.IN)
GPIO.setup(ROCKET_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

channels = []
channels.append(AnalogIn(ads, ADS.P0))
channels.append(AnalogIn(ads, ADS.P1))
channels.append(AnalogIn(ads, ADS.P2))
channels.append(AnalogIn(ads, ADS.P3))



def is_ir_detected():
    # print(channels[IR_SENSOR_ANALOG_PIN].voltage)
    return channels[IR_SENSOR_ANALOG_PIN].voltage > IR_TRIGGER_VOLTAGE

def is_light_detected():
    voltage = channels[LIGHT_SENSOR_ANALOG_PIN].voltage
    print(voltage)
    return voltage < LIGHT_TRIGGER_VOLTAGE

   
def check_ir():
    while True:
        if is_ir_detected():
            print("IR detected!")
            print("Activating hovercraft...")
            enable_hovercraft()
            time.sleep(HOVERCRAFT_TIME)
            print(f"Stopping hovercraft after {HOVERCRAFT_TIME}s...")
            disable_hovercraft()
            return
        if stop_detecting:
            return
        time.sleep(0.025)

def check_light():
    same = 0
    while True:
        if is_light_detected():
            same += 1
        else:
            same = 0
        if same >= LIGHT_SENSOR_SURE:
            print("Rocket detected!")
            stop_rocket()
            return
        if stop_detecting:
            return
        time.sleep(0.025)
    
            
def enable_hovercraft():
    GPIO.output(RELAY_PIN, GPIO.HIGH)


def disable_hovercraft():
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
    GPIO.output(ROCKET_PIN, GPIO.HIGH)

def stop_rocket():
    print("Stopping rocket...")
    GPIO.output(ROCKET_PIN, GPIO.LOW)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5) #nog aanpassen
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(BUZZER_PIN, GPIO.LOW)


    

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
        GPIO.output(ROCKET_PIN, GPIO.LOW)
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        GPIO.cleanup()

