import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

EPSReset = 6

print("Resetting EPS")
GPIO.setup(EPSReset, GPIO.OUT, initial=GPIO.HIGH)
GPIO.output(EPSReset, GPIO.LOW)
sleep(1)
GPIO.output(EPSReset, GPIO.HIGH)
print("EPS Reset")
GPIO.cleanup()
