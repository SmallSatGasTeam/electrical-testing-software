import spidev
spi0 = spidev.SpiDev()
spi0.open(0, 0)

spi1 = spidev.SpiDev()
spi1.open(0, 1)

temp0_raw = spi0.readbytes(2)  #Read just the first 13 bits, as the last three bits of the 16 byte word are not used
temp1_raw = spi1.readbytes(2)  

print("Raw data temp0: ")
print(temp0_raw)

print("Raw data temp1: ")
print(temp1_raw)

#This function converts the two bytes to the temperature value. The data is stored as two bytes where T13 is the most significant bit
#| T13 T12 T11 T10 T9 T8 T7 T6 |  | T5 T4 T3 T2 T1 1 1 1 |
temp0 = ((temp0_raw[0] * 512) + (temp0_raw[1] - 7)* 0.0625
temp1 = ((temp1_raw[0] * 512) + (temp1_raw[1] - 7)* 0.0625

print("temp0: ")
print(temp0)

print("temp1: ")
print(temp1)

spi0.close()
spi1.close()
