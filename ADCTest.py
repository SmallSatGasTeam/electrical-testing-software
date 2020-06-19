import spidev
import RPi.GPIO as GPIO

adc_cs = 22
sclk = 23
miso = 21
mosi = 19

GPIO.setmode(GPIO.BOARD)
GPIO.setup(adc_cs, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(sclk, GPIO.OUT)
GPIO.setup(miso, GPIO.IN)
GPIO.setup(mosi, GPIO.OUT)

input("Connecting to ADC, press <Enter> to continue...")

spi = spidev.SpiDev()
spi.open(0,0)
spi.no_cs = True
GPIO.output(adc_cs, GPIO.LOW)
GPIO.output(sclk, GPIO.LOW)

input("Getting data from UV sensor, channel 1, press <Enter> to continue...")

msg = 0b11
msg = ((msg << 1) + 1) << 5
msg = [msg, 0b00000000]
uv_sense = spi.xfer2(msg)
print("UV sensor value: ")
print(uv_sense)

input("Getting data from Sun sensor 1, channel 5, press <Enter> to continue...")

msg = 0b11
msg = ((msg << 1) + 5) << 5
msg = [msg, 0b00000000]
sun1 = spi.xfer2(msg)
print("Sun sensor 1 value: ")
print(sun1)

input("Getting data from Sun sensor 2, channel 4, press <Enter> to continue...")

msg = 0b11
msg = ((msg << 1) + 4) << 5
msg = [msg, 0b00000000]
sun2 = spi.xfer2(msg)
print("Sun sensor 2 value: ")
print(sun2)

input("Getting data from Sun sensor 3, channel 2, press <Enter> to continue...")

msg = 0b11
msg = ((msg << 1) + 2) << 5
msg = [msg, 0b00000000]
sun3 = spi.xfer2(msg)
print("Sun sensor 3 value: ")
print(sun3)

input("Getting data from Sun sensor 4, channel 3, press <Enter> to continue...")

msg = 0b11
msg = ((msg << 1) + 3) << 5
msg = [msg, 0b00000000]
sun4 = spi.xfer2(msg)
print("Sun sensor 4 value: ")
print(sun4)

input("Getting data from Sun sensor 5, channel 0, press <Enter> to continue...")

msg = 0b11
msg = ((msg << 1) + 0) << 5
msg = [msg, 0b00000000]
sun5 = spi.xfer2(msg)
print("Sun sensor 5 value: ")
print(sun5)


GPIO.output(adc_cs, GPIO.HIGH)
GPIO.output(sclk, GPIO.HIGH)

spi.close()
GPIO.cleanup()
