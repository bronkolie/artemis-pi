
import time, board, busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus (I2C must be ENABLED on the Pi!!)
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

channels = []

channels.append(AnalogIn(ads, ADS.P0))
channels.append(AnalogIn(ads, ADS.P1))



def print_IR():
    start_time = time.time()
    while True:
        
        voltage = channels[0].voltage
        # if voltage > 1.75:
        #     print(f"IR detected after {round(time.time() - start_time, 3)}s")
        #     break
        print(voltage)
        time.sleep(0.025)



if __name__ == "__main__":
    print_IR()
