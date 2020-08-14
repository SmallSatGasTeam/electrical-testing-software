import spidev
import RPi.GPIO as GPIO

temp0_ch = 0
temp1_ch = 1

adc_cs = 22
sclk = 23
miso = 21
mosi = 19

GPIO.setmode(GPIO.BOARD)
GPIO.setup(adc_cs, GPIO.OUT, initial=GPIO.HIGH)
#GPIO.setup(sclk, GPIO.OUT)
#GPIO.setup(miso, GPIO.IN)
#GPIO.setup(mosi, GPIO.OUT)

input("Testing connection to ADC, press <Enter> to continue...")

spi = spidev.SpiDev()
spi.open(0,0)
spi.no_cs = True
GPIO.output(adc_cs, GPIO.LOW)
#GPIO.output(sclk, GPIO.LOW)

msg = 0b11
msg = ((msg << 1) + 1) << 5
msg = [msg, 0b00000000]

reply = spi.xfer2(msg)
print("Reply from ADC: ")
print(reply)

GPIO.output(adc_cs, GPIO.HIGH)
#GPIO.output(sclk, GPIO.HIGH)

spi.close()


input("Testing connection to Temp0, press <Enter> to continue...")

spi = spidev.SpiDev()
spi.open(0,0)
spi.no_cs = False

reply = spi.readbytes(2)
print("Reply from Temp0: ")
print(reply)

spi.close()


input("Testing connection to Temp1, press <Enter> to continue...")

spi = spidev.SpiDev()
spi.open(0,1)
spi.no_cs = False

reply = spi.readbytes(2)
print("Reply from Temp1: ")
print(reply)

spi.close()

GPIO.cleanup()
