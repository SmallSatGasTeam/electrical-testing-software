from time import sleep
import datetime
import board
import busio
import adafruit_lsm303_accel
import adafruit_lsm303dlh_mag   #This is for the breakout board

i2c = busio.I2C(board.SCL, board.SDA)
mag = adafruit_lsm303dlh_mag.LSM303DLH_Mag(i2c)
accel = adafruit_lsm303_accel.LSM303_Accel(i2c)

while True:
  accelStr = str(accel.acceleration)
  magStr = str(mag.magnetic)
  timestamp = str(datetime.datetime.now())
  filename = "./data/magData" + timestamp + ".txt"
  
  dataFile = open(filename, "w")
  
  dataFile.write(timestamp + "\n")
  dataFile.write(accelStr + "\n")
  dataFile.write(magStr + "\n")
  
  dataFile.close()
  sleep(0.05)
