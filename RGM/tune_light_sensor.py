import RPi.GPIO as GPIO
import time, board, busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import configparser


def setup():
    config = configparser.ConfigParser(inline_comment_prefixes="#")
    config.read('rgm.conf')


    SDA_PIN = int(config['digital_pins']['sda'])
    SCL_PIN = int(config['digital_pins']['scl'])

    LIGHT_TRIGGER_VOLTAGE = float(config['trigger_voltages']['light_sensor'])


    LIGHT_SENSOR_ANALOG_PIN = int(config['analog_pins']['light_sensor'])


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

    return LIGHT_TRIGGER_VOLTAGE, LIGHT_SENSOR_ANALOG_PIN, channels


def print_voltage(LIGHT_TRIGGER_VOLTAGE, LIGHT_SENSOR_ANALOG_PIN, channels):
    voltage = channels[LIGHT_SENSOR_ANALOG_PIN].voltage
    if voltage > LIGHT_TRIGGER_VOLTAGE:
        print(f"No rocket detected at {voltage}v")
    else:
         print(f"Rocket detected at {voltage}v")

def main():
    LIGHT_TRIGGER_VOLTAGE, LIGHT_SENSOR_ANALOG_PIN, channels = setup()
    start = time.time()
    while True:
        print_voltage(LIGHT_TRIGGER_VOLTAGE, LIGHT_SENSOR_ANALOG_PIN, channels)
        if time.time() - start > 0.5:
            start = time.time()
            LIGHT_TRIGGER_VOLTAGE, LIGHT_SENSOR_ANALOG_PIN, channels = setup()
        time.sleep(0.025)

try:
    main()
except KeyboardInterrupt:
    print("\nInterrupted. Exiting...")
        