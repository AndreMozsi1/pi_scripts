import OPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setboard(GPIO.PCPCPLUS) # Set the board to PC Plus
GPIO.setmode(GPIO.SUNXI) # Set the mode to SUNXI pin numbering
GPIO.setup("PA10", GPIO.OUT) # Set up pin PA10 as an output pin

# Loop forever
while True:
    # Turn on the LED
    GPIO.output("PA10", GPIO.HIGH)
    # Wait for half a second
    time.sleep(0.5)
    # Turn off the LED
    GPIO.output("PA10", GPIO.LOW)
    # Wait for half a second
    time.sleep(0.5)