import spidev
import RPi.GPIO as GPIO
import time

# Setup SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device (CS) 0
spi.max_speed_hz = 1350000

# Function to read from the MCP3008
def read_channel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.OUT)

try:
    while True:
        GPIO.output(6, GPIO.HIGH)
        time.sleep(0.0005)  # delayMicroseconds(500)
        a = read_channel(3)  # Reading from channel A3
        GPIO.output(6, GPIO.LOW)
        time.sleep(0.0005)  # delayMicroseconds(500)
        b = read_channel(3)  # Reading from channel A3
        c = a - b
        print(c)
        time.sleep(0.1)  # Small delay to prevent excessive CPU usage
finally:
    spi.close()
    GPIO.cleanup()