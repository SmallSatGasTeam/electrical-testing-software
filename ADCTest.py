import spidev
import time
import RPi.GPIO as GPIO
from time import sleep

adc_cs = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(adc_cs, GPIO.OUT, initial=GPIO.HIGH)

#input("Connecting to ADC, press <Enter> to continue...")

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000
spi.no_cs = True

while True:
    print("-------------------------")

    GPIO.output(adc_cs, GPIO.HIGH)

    #input("Getting data from UV sensor, channel 1, press <Enter> to continue...")

    GPIO.output(adc_cs, GPIO.LOW)
    sleep(.01)
    msg = [0b00001000, 0b00000000]
    uv_sense = spi.xfer2(msg)
    uv_sense = spi.xfer2(msg)
    GPIO.output(adc_cs, GPIO.HIGH)
    uv_val = (uv_sense[1] + (uv_sense[0] * 256))*(3.3/4096)   #Converts the 12 bit serial signal to the voltage
    #print("UV sensor value: ")
    #print(uv_sense)
    #print(uv_val)

    #input("Getting data from Sun sensor 1, channel 5, press <Enter> to continue...")

    GPIO.output(adc_cs, GPIO.LOW)
    sleep(.01)
    msg = [0b00101000, 0b00000000]
    sun1 = spi.xfer2(msg)
    sun1 = spi.xfer2(msg)
    GPIO.output(adc_cs, GPIO.HIGH)
    sun1_val = (sun1[1] + (sun1[0] * 256))*(3.3/4096)   #Converts the 12 bit serial signal to the voltage
    #print("Sun sensor 1 value: ")
    #print(sun1)
    #print(sun1_val)

    #input("Getting data from Sun sensor 2, channel 4, press <Enter> to continue...")

    GPIO.output(adc_cs, GPIO.LOW)
    sleep(.01)
    msg = [0b00100000, 0b00000000]
    sun2 = spi.xfer2(msg)
    sun2 = spi.xfer2(msg)
    GPIO.output(adc_cs, GPIO.HIGH)
    sun2_val = (sun2[1] + (sun2[0] * 256))*(3.3/4096)   #Converts the 12 bit serial signal to the voltage
    #print("Sun sensor 2 value: ")
    #print(sun2)
    #print(sun2_val)

    #input("Getting data from Sun sensor 3, channel 2, press <Enter> to continue...")

    GPIO.output(adc_cs, GPIO.LOW)
    sleep(.01)
    msg = [0b00010000, 0b00000000]
    sun3 = spi.xfer2(msg)
    sun3 = spi.xfer2(msg)
    GPIO.output(adc_cs, GPIO.HIGH)
    sun3_val = (sun3[1] + (sun3[0] * 256))*(3.3/4096)   #Converts the 12 bit serial signal to the voltage
    #print("Sun sensor 3 value: ")
    #print(sun3)
    #print(sun3_val)

    #input("Getting data from Sun sensor 4, channel 3, press <Enter> to continue...")

    GPIO.output(adc_cs, GPIO.LOW)
    sleep(.01)
    msg = [0b00011000, 0b00000000]
    sun4 = spi.xfer2(msg)
    sun4 = spi.xfer2(msg)
    GPIO.output(adc_cs, GPIO.HIGH)
    sun4_val = (sun4[1] + (sun4[0] * 256))*(3.3/4096)   #Converts the 12 bit serial signal to the voltage
    #print("Sun sensor 4 value: ")
    #print(sun4)
    #print(sun4_val)

    #input("Getting data from Sun sensor 5, channel 0, press <Enter> to continue...")

    GPIO.output(adc_cs, GPIO.LOW)
    sleep(.01)
    msg = [0b00000000, 0b00000000]
    sun5 = spi.xfer2(msg)
    sun5 = spi.xfer2(msg)
    GPIO.output(adc_cs, GPIO.HIGH)
    sun5_val = (sun5[1] + (sun5[0] * 256))*(3.3/4096)   #Converts the 12 bit serial signal to the voltage
    #print("Sun sensor 5 value: ")
    #print(sun5)
    #print(sun5_val)

    print("1\t\t2\t\t3\t\t4\t\t5\t\tUV")
    print("%.7f \t" % sun1_val, end="")
    print("%.7f \t" % sun2_val, end="")
    print("%.7f \t" % sun3_val, end="")
    print("%.7f \t" % sun4_val, end="")
    print("%.7f \t" % sun5_val, end="")
    print("%.7f" % uv_val)

spi.close()
GPIO.cleanup()

