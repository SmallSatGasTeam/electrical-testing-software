# Wirecutters testing code
# Nik Clark
# 4/11/2020

# This script will allow the user to fire the burn wire mechanism while controlling the 
# PWM settings for the on pins. Note that 100 Hz might be the fastest PWM frequency,
# some research implies that higher frequencies might make the start() function call blocking.

class WireCutter:
    def __init__( self, p_name, p_on, p_safety1, p_safety2 ):
        self.name = p_name
        
        # initialize pins
        GPIO.setup( p_safety1, GPIO.OUT, initial=GPIO.LOW )
        GPIO.setup( p_safety2, GPIO.OUT, initial=GPIO.LOW )
        GPIO.setup( p_on, GPIO.OUT, initial=GPIO.HIGH )
        
        #define the pinout. The on signal is PWM with a frequency of 100 Hz
        self.onpin = p_on
        # self.on = GPIO.PWM(p_on, 10)
        self.safety1 = p_safety1
        self.safety1 = GPIO.PWM(p_safety1, 500)
        self.safety2 = p_safety2

        self.duty_cycle = 75.0
        self.safety1.ChangeDutyCycle(self.duty_cycle)
        
        
        self.burn_time = 5.0

        # Allow user to verify settings
        print( "GPIO initialized for: ", self.name, ". Burn wire should be OFF" )
        
    def set_duty_cycle( self, p_duty_cycle):
        if( p_duty_cycle <= 100.0 and p_duty_cycle > 0 ):
            self.duty_cycle = p_duty_cycle
            self.safety1.ChangeDutyCycle(self.duty_cycle)
            print("duty cycle set to {}".format(self.duty_cycle))
            
    def set_burn_time( self, p_burn_time ):
        if p_burn_time > 0 and p_burn_time < 5:
            self.burn_time = p_burn_time
            
    def fire( self ):
        # Fire burn wire
        print("{} is on".format(self.name))
        GPIO.output(self.onpin, GPIO.LOW)
        #GPIO.output(self.safety1, GPIO.HIGH)
        GPIO.output(self.safety2, GPIO.HIGH)
        self.safety1.start(self.duty_cycle)
        
        # Burn for the set amount of seconds (between 0 and 5)
        sleep(self.burn_time)

        # Turn burn wire off
        self.safety1.stop()
        GPIO.output( self.onpin, GPIO.HIGH)
        #GPIO.output( self.safety1, GPIO.LOW )
        GPIO.output( self.safety2, GPIO.LOW )
        print("{} is off".format(self.name))



import RPi.GPIO as GPIO
from time import sleep

def main():
    # Define that we are using physical pin numbers
    GPIO.setmode(GPIO.BOARD)
    #GPIO.setmode(GPIO.BCM)

    # Create 2 WireCutter Objects for each burn wire
    # The constructors for each object will initialize each to its completely OFF state
    if GPIO.getmode() == GPIO.BOARD:
        WC1 = WireCutter( "WC1", 7, 38, 36 )
        WC2 = WireCutter( "WC2", 29, 37, 35 )
    elif GPIO.getmode() == GPIO.BCM:
        WC1 = WireCutter( "WC1", 4, 20, 16 )
        WC2 = WireCutter( "WC2", 5, 26, 19 )
        
    # Test burn wires with varying duty cycles until power is limited.
    wcChoice = input("Enter wirecutter to test <1,2>: ")
    if(wcChoice == '1'):
        WC = WC1
    elif(wcChoice == '2'):
        WC = WC2
    else:
        WC = WC1
        print("Invalid input, defaulting to wirecutter 1")
    
    selection = '1'
    while (selection == '1'):

        dc_val = input("Enter duty cycle between 0 and 100: ")
        WC.set_duty_cycle(float(dc_val))
        WC.fire()

        # cleanup and end program
        selection = input("All tests completed. Press <1> to run test again. Any other key to exit. " )
    GPIO.cleanup()


if __name__ == "__main__":
    main()
