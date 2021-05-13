import RPi.GPIO as GPIO
from time import sleep

EPSReset = 6

print("Resetting EPS")
GPIO.setup(EPSReset, GPIO.OUT, initial=GPIO.HIGH)
GPIO.output(EPSReset, GPIO.LOW)
sleep(0.5)
GPIO.output(EPSReset, GPIO.HIGH)
print("EPS Reset")
GPIO.cleanup()
