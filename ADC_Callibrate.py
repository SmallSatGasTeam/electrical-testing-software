import numpy as np
import spidev
import RPi.GPIO as GPIO
import sys

adc_cs = 22
spi = spidev.SpiDev()

def calculate_regression(expected, measured, error):
    if len(expected) == len(measured):
        # Setup matrices
        Y = np.array([expected])
        Y = np.transpose(Y)
        X = np.array([measured])
        X = np.transpose(X)
        X = np.concatenate( (np.ones_like(X),X), axis=1 )
        
        # Solve for the coefficients of the linear equation
        B = np.matmul(np.transpose(X),X)
        B = np.linalg.inv(B)
        B = np.matmul(B,np.transpose(X))
        B = np.matmul(B,Y)

        # Return the coefficients and the error vector
        e_array = np.add(Y, -np.matmul(X,B))
        for i in e_array:
            error.append(float(i))
        return B

    return 0
    
def getSample(channel):
    GPIO.output(adc_cs, GPIO.LOW)
    msg = [0b00001000, 0b00000000]
    uv_sense = spi.xfer2(msg)
    uv_sense = spi.xfer2(msg)
    GPIO.output(adc_cs, GPIO.HIGH)
    uv_val = (uv_sense[1] + (uv_sense[0] * 256))*(3.3/4096)   #Converts the 12 bit serial signal to the voltage
    return uv_val

def main():
#    sys.stdout = open("ADC_callibration_constants.txt", "w")  #Comment this line to have values printed to console instead 
   
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(adc_cs, GPIO.OUT, initial=GPIO.HIGH)

    # Setup ADC
    input("Connecting to ADC, press <Enter> to continue...")

    spi.open(0,0)
    spi.max_speed_hz = 1000
    spi.no_cs = True
    GPIO.output(adc_cs, GPIO.HIGH)

    # Samples need to be taken across the full range of the output up to 3V3
    numSamples = int(input("Enter the number of samples to be taken per channel: "))
    numChannels = int(input("Enter the number of channels to be calibrated: "))
    expected = []
    measured = []
    
    for chan in range(numChannels):
        x = input("Connect voltage supply to channel {}".format(chan))
        for voltage in range(numSamples):
            x = input("Set supply to {} volts".format(round((voltage*3.3)/numSamples,2)))
            expected.append(round((voltage*3.3)/numSamples,2))
            measured.append(getSample(chan))
            
        print("For channel {}:".format(chan))
        print("measured voltages: {}".format(measured))
        print("expected voltages: {}".format(expected)) 

        reg_error = []
        raw_error = []

        #calculate raw error
        for i in range(len(expected)):
            raw_error.append(abs(expected[i] - measured[i]))

        print('Maximum error before regression: {}'.format(max(raw_error)))

        B = calculate_regression(expected, measured, reg_error)

        print('Maximum error after regression: {}'.format(max(reg_error)))
        print('Regression coefficients: ')
        print(B)

    spi.close()
    GPIO.cleanup()
    if sys.stdout.name != '<stdout>':
        sys.stdout.close()

if __name__ == "__main__":
    main()
