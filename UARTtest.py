import serial

ser = serial.Serial ("/dev/ttyAMA0")    #Open named port 
ser.baudrate = 9600                     #Set baud rate to 9600
data = "a"                              #Set data to the character 'a', 0x61 or 01100001
ser.write(data)                         #Send the data
ser.close()
