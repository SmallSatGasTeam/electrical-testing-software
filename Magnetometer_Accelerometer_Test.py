#Make sure the following libraries are installed:
#   sudo pip3 install RPI.GPIO
#   sudo pip3 install adafruit-blinka
#   sudo pip3 install adafruit-circuitpython-lsm303-accel
#   For LSM303AGR:
#     sudo pip3 install adafruit-circuitpython-lis2mdl
#   For LSM303DLH:
#     sudo pip3 install adafruit-circuitpython-lsm303dlh-mag


import board
import busio
import adafruit_lsm303_accel

#for LSM303AGR
import adafruit_lis2mdl
#for LSM303DLH
#import adafruit_lsm303dlh_mag

#Set up I2C link
i2c = busio.I2C(board.SCL, board.SDA)

#Set up link to accelerometer
accel = adafruit_lsm303_accel.LSM303_Accel(i2c)

#Set up link to magnetometer
#for LSM303AGR
mag = adafruit_lis2mdl.LIS2MDL(i2c)
#for LSM303DLH
#mag = adafruit_lis2mdl.LSM303DLH_Mag(i2c)

#Print values
print (“Acceleration (m/s^2): X=%0.3f Y=%0.3f Z=%0.3f”%accel.acceleration) 
print (“Magnetometer (uTeslas): X=%0.3f Y=%0.3f Z=%0.3f”%mag.magnetic) 
