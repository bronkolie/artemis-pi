print("Hello World")  # say hi :)
import RPi.GPIO as GPIO  # aquire knowledge about controlling the Raspberry pins. Name the library as GPIO, to reference in our code (we otherwise have to type RPi.GPIO completely everytime)

GPIO.setmode(GPIO.BCM)  # Set the pin numbering as we expect, so it is aligned with the breadboard numbering

ledPin = 4  # Choose the pin number which we use to output power towards the LED
GPIO.setup(ledPin, GPIO.OUT)  # Actually assign the pin of the Raspberry to output power, instead of using the pin as input (reading signals)


import time  # acquire knowledge about methods regarding time.

startTime = time.time()  # acquire the current timestamp (is counting since 1 January 1970).
print(startTime)  # see the timestamp number. (float)


while (time.time() - startTime < 5):   # start looping with a duration of 5 seconds: time.time() = current time  ||  substract startTime to acquire elapsed time in seconds.
    GPIO.output(ledPin , GPIO.HIGH)  # Tell Raspberry to output power over the pin we assigned earlier. 
    time.sleep(1)   # pause our script for 1 second
    GPIO.output(ledPin , GPIO.LOW)   # Tell Raspberry to stop providing power over the LED pin.
    time.sleep(1)   # wait again for 1 second and thereafter go back to the beginnen of the while loop.

# we arrive here when the loop has stopped (after 5 seconds)
print("LED has blinked for 5 seconds and should now be turned off. Exiting script...")
