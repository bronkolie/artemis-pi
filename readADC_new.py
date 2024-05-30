''' PIN SETUP (example of ADS1115 + potentiometer)
GPIO 2 = SDA     GPIO 3 = SCL
GND = GND   VDD = 3.3V  (or 5V depending on analog sensors)

A0 = center pin potentiometer
left pin potentiometer = 3.3V
right pin potentiometer = GND

ENABLE I2C on the Raspberry: open VNC viewer -> open terminal ->
    enter: sudo raspi-config    -> Interface Options -> I2C
'''
import time, board, busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus (I2C must be ENABLED on the Pi!!)
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

channels = []
# Create single-ended input on channel 0
channels.append(AnalogIn(ads, ADS.P0))

print(f"{'raw':>5}\t{'v':>5}")
start_time = time.time()
while True:
    for idx, channel in enumerate(channels):
        print(f"channel {idx}: {channel.value}, {channel.voltage:.3f}\t", end='')
    print(end='\n')
    time.sleep(0.025)