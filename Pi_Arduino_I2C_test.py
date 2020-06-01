import smbus

address = 0x08

bus = smbus.SMBus(1)

def writeNumber(value):
  bus.write_byte(address,value)
  print value
  
if __name__ == "__main__":
  while(True):
    valueInput = input("Input a number: ")
    value = int(valueInput)
    writeNumber(value)
