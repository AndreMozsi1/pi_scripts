import wiringpi
import time

LED_PIN = 2

wiringpi.wiringPiSetup()
wiringpi.pinMode(LED_PIN, wiringpi.GPIO.OUTPUT)

while True:
    wiringpi.digitalWrite(LED_PIN, wiringpi.GPIO.HIGH) # Turn LED on
    time.sleep(0.5) # Wait for 0.5 seconds
    wiringpi.digitalWrite(LED_PIN, wiringpi.GPIO.LOW) # Turn LED off
    time.sleep(0.5) # Wait for 0.5 seconds
