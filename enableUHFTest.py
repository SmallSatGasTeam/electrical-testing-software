import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

UHFEn = 24

GPIO.setup(UHFEn, GPIO.OUT, initial=GPIO.HIGH)
print("Enabling UHF...")
GPIO.output(UHFEn, GPIO.HIGH)
input("UHF Enabled, Press enter to continue")
print("Disabling UHF...")
GPIO.output(UHFEn, GPIO.LOW)
print("UHF Disabled, Press enter to continue")
GPIO.output(UHFEn, GPIO.HIGH)
GPIO.cleanup()
