from time import sleep
import smbus

bus = smbus.SMBus(1)

address = 0x08

def writeNumber(value):
    bus.write_byte(address, value)

if __name__ == "__main__":
    while True:
        valueInput = input("Inpute a value: ")    
        value = int(valueInput)
        writeNumber(value)
   
  
 
