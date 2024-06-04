import RPi.GPIO as GPIO
import time, board, busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import configparser
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))

def setup():
    config = configparser.ConfigParser(inline_comment_prefixes="#")
    config.read('rgm.conf')


    SDA_PIN = int(config['digital_pins']['sda'])
    SCL_PIN = int(config['digital_pins']['scl'])

    IR_TRIGGER_VOLTAGE = float(config['trigger_voltages']['ir_sensor'])


    IR_SENSOR_ANALOG_PIN = int(config['analog_pins']['ir_sensor'])


    class WrongWiringException(Exception):
        def __init__(self, message="The ADC was wired incorrectly.\nSDA must be connected to GPIO pin 2 and SCL must be connected to GPIO pin 3"):
            self.message = message
            super().__init__(self.message)

    if SDA_PIN != 2 or SCL_PIN != 3:
        raise WrongWiringException()


    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)

    channels = []
    channels.append(AnalogIn(ads, ADS.P0))
    channels.append(AnalogIn(ads, ADS.P1))
    channels.append(AnalogIn(ads, ADS.P2))
    channels.append(AnalogIn(ads, ADS.P3))

    return IR_TRIGGER_VOLTAGE, IR_SENSOR_ANALOG_PIN, channels


def print_voltage(IR_TRIGGER_VOLTAGE, IR_SENSOR_ANALOG_PIN, channels):

    voltage = channels[IR_SENSOR_ANALOG_PIN].voltage
    if voltage > IR_TRIGGER_VOLTAGE:
        print(f"IR detected at {voltage}v")
    else:
         print(f"No IR detected at {voltage}v")

def main():
    IR_TRIGGER_VOLTAGE, IR_SENSOR_ANALOG_PIN, channels = setup()
    start = time.time()
    while True:
        print_voltage(IR_TRIGGER_VOLTAGE, IR_SENSOR_ANALOG_PIN, channels)
        if time.time() - start > 0.5:
            start = time.time()
            IR_TRIGGER_VOLTAGE, IR_SENSOR_ANALOG_PIN, channels = setup()
        time.sleep(0.025)

try:
    main()
except KeyboardInterrupt:
    print("\nInterrupted. Exiting...")
        
