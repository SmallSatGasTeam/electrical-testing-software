# Wirecutters testing code
# Nik Clark
# 4/11/2020

# This code will test the inhibit system for each burn wire mechanism. In succession.
# for each redundant system the inputs will be toggled in succession. Only in the final
# iteration should the burn wire mechanism allow current to flow. These states will be designated
# in the console and with the debugging LEDs on board.


class WireCutter:
    def __init__( self, p_name, p_on, p_safety1, p_safety2 ):
        self.name = p_name
        
        # initialize pins
        GPIO.setup( p_safety1, GPIO.OUT, initial=GPIO.LOW )
        GPIO.setup( p_safety2, GPIO.OUT, initial=GPIO.LOW )
        GPIO.setup( p_on, GPIO.OUT, initial=GPIO.HIGH )
        
        #define the pinout. The on signal is PWM with a frequency of 100 Hz
        self.on = GPIO.PWM(p_on, 100)
        self.duty_cycle = 100.0
        self.on.ChangeDutyCycle(self.duty_cycle)
        
        self.safety1 = p_safety1
        self.safety2 = p_safety2  
        
        self.burn_time = 2.0

        # Allow user to verify settings
        print( "GPIO initialized for: ", self.name, ". Burn wire should be OFF" )
        
    def set_duty_cycle( self, p_dutycyle):
        if( p_duty_cycle <= 100.0 and p_duty_cycle > 0 ):
            self.duty_cycle = p_duty_cycle
            self.on.ChangeDutyCycle(self.duty_cycle)
            
    def set_burn_time( self, p_burn_time ):
        if p_burn_time > 0 and p_burn_time < 5:
            self.burn_time = p_burn_time
            
    def fire( self ):
        # Fire burn wire
        print("{} is on".format(self.name))
        self.on.start(self.duty_cycle)
        GPIO.output( self.safety1, GPIO.HIGH )
        GPIO.output( self.safety2, GPIO.HIGH )
        
        # Burn for the set amount of seconds (between 0 and 5)
        sleep(self.burn_time)

        # Turn burn wire off
        self.on.stop()
        GPIO.output( self.on, GPIO.HIGH)
        GPIO.output( self.safety1, GPIO.LOW )
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

    # cleanup and end program
    input("All tests completed. Exiting program. Press <ENTER> to quit." )
    GPIO.cleanup()


if __name__ == "__main__":
    main()
