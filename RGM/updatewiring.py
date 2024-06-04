import configparser
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


config = configparser.ConfigParser(inline_comment_prefixes="#")
config.read('rgm.conf')

BUTTON_PIN = config['digital_pins']['button']
IMPACT_SENSOR_PIN = config['digital_pins']['impact_sensor']
IR_LED_PIN = config['digital_pins']['ir_led']
RELAY_PIN = config['digital_pins']['relay']
ROCKET_PIN = config['digital_pins']['rocket']
SDA_PIN = config['digital_pins']['sda']
SCL_PIN = config['digital_pins']['scl']

IR_SENSOR_ANALOG_PIN = config['analog_pins']['ir_sensor']
LIGHT_SENSOR_ANALOG_PIN = config['analog_pins']['light_sensor']

class WrongWiringException(Exception):
    def __init__(self, message="The ADC was wired incorrectly.\nSDA must be connected to GPIO pin 2 and SCL must be connected to GPIO pin 3"):
        self.message = message
        super().__init__(self.message)

if int(SDA_PIN) != 2 or int(SCL_PIN) != 3:
    raise WrongWiringException()

schematic = (f"""Pi:      ADC:         Impact sensor:         Relay:     ROCKET:        IR sensor     1MOhm resistor       Light sensor     Button:      IR LED:
{SDA_PIN} ------ SDA
{SCL_PIN} ------ SCL           
{IMPACT_SENSOR_PIN} ----------------------- OUT
{RELAY_PIN} ------------------------------------------- SIG
{ROCKET_PIN} -------------------------------------------------------- G+
         A{IR_SENSOR_ANALOG_PIN} ------------------------------------------------------------- AOUT
         A{LIGHT_SENSOR_ANALOG_PIN} ----------------------------------------------------------------------------- 1
                                                                                          2 ------------------ OUT    
                                                                                                                              OUT ---------- C
GND ---- GND ------------ GND ---------------- GND -------- GND ---------- GND ------------------------------- GND ---------- GND
5V ----- VDD ------------ +5V ---------------- VCC ----------------------- +5V ------------------------------- +5V
3V -------------------------------------------------------------------------------------------------------------------------- +5V ---------- A""")

wiring = open("wiring.txt", "w")
wiring.write(schematic)
