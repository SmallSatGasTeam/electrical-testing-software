import RPi.GPIO as GPIO
from time import sleep

#Pin numbers for AD_primary and AD_secondary using GPIO numbering scheme
AD_primary = 13
AD_secondary = 12

#Setup AD_primary and AD_secondary as outputs with initial setting LOW
GPIO.setup(AD_primary, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(AD_secondary, GPIO.OUT, initial=GPIO.LOW)

input("Turning on AD_primary. Press <ENTER> to continue")
GPIO.output(AD_primary, GPIO.HIGH)
sleep(0.5)
GPIO.output(AD_primary, GPIO.LOW)
print("AD_primary was switched on.")

input("Turning on AD_secondary. Press <ENTER> to continue")
GPIO.output(AD_secondary, GPIO.HIGH)
sleep(0.5)
GPIO.output(AD_secondary, GPIO.LOW)
print("AD_secondary was switched on.")
GPIO.cleanup()
