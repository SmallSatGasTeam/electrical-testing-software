import spidev
spi0 = spidev.SpiDev()
spi0.open(0, 0)

spi1 = spidev.SpiDev()
spi1.open(0, 1)

temp0_raw = spi0.readbytes(13)  #Read just the first 13 bits, as thelast three bits of the 16 byte word are not used
temp1_raw = spi1.readbytes(13)  

print("Raw data temp0: ")
print(temp0_raw)

print("Raw data temp1: ")
print(temp1_raw)

temp0 = temp0_raw * 0.0625
temp1 = temp1_raw * 0.0625

print("temp0: ")
print(temp0)

print("temp1: ")
print(temp1)

spi0.close()
spi1.close()
