import RPi.GPIO as GPIO
import time
import time, board, busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn



READ_ADC = False
GPIO.setmode(GPIO.BCM)


# Set up the motion sensor GPIO pin
MOTION_SENSOR_PIN = 5
GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)

if READ_ADC:
    i2c = busio.I2C(board.SCL, board.SDA)
    ads = ADS.ADS1115(i2c)
    channels = []
    channels.append(AnalogIn(ads, ADS.P0))
    channels.append(AnalogIn(ads, ADS.P1))


counter = 0
try:
    while True:
        if GPIO.input(MOTION_SENSOR_PIN) == 0:
            if not READ_ADC:
                print(f"Motion detected! ({counter})")
            else:
                voltage = channels[1].voltage
                print(f"Motion detected with {voltage}V")
            counter += 1
            time.sleep(0.1)
        # else:
        #     print("No motion detected")
        # time.sleep(0.0)  # Adjust the sleep time as needed
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()

