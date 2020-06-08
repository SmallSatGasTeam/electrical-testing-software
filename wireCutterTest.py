# Wirecutters testing code
# Nik Clark
# 4/11/2020

# This code will test the inhibit system for each burn wire mechanism. In succession.
# for each redundant system the inputs will be toggled in succession. Only in the final
# iteration should the burn wire mechanism allow current to flow. These states will be designated
# in the console and with the debugging LEDs on board.


class WireCutter:
    def __init__( self, p_name, p_on, p_safety1, p_safety2, p_ledr, p_ledg, p_ledy ):
        self.name = p_name
        #define the pinout
        self.on = p_on
        self.safety1 = p_safety1
        self.safety2 = p_safety2
        self.LED_red = p_ledr
        self.LED_green = p_ledg
        self.LED_yellow = p_ledy

        # initialize pins
        GPIO.setup( self.safety1, GPIO.OUT, initial=GPIO.LOW )
        GPIO.setup( self.safety2, GPIO.OUT, initial=GPIO.LOW )
        GPIO.setup( self.on, GPIO.OUT, initial=GPIO.HIGH )

        # Allow user to verify settins
        print( "GPIO initialized for: ", self.name, ". Burn wire should be OFF" )
        input("press <ENTER> to continue")


    def set_state_wait( self, p_on, p_safety1, p_safety2 ):
        GPIO.output( self.on, p_on )
        GPIO.output( self.safety1, p_safety1 )
        GPIO.output( self.safety2, p_safety2 )
        print("    ", self.name, "_on: ", p_on )
        print("    ", self.name, "_safety1: ", p_safety1 )
        print("    ", self.name, "_safety2: ", p_safety2 )

        if p_on==GPIO.LOW and p_safety1==GPIO.HIGH and p_safety2==GPIO.HIGH:
            GPIO.output( self.LED_green, GPIO.LOW )
            GPIO.output( self.LED_red, GPIO.HIGH )
            input("Wirecutter should be on. Press <ENTER> to continue")
        else:
            GPIO.output( self.LED_green, GPIO.HIGH )
            GPIO.output( self.LED_red, GPIO.LOW )
            input("Wirecutter should be off. Press <ENTER> to continue")

    def set_state( self, p_on, p_safety1, p_safety2 ):
        GPIO.output( self.on, p_on )
        GPIO.output( self.safety1, p_safety1 )
        GPIO.output( self.safety2, p_safety2 )
        print("    ", self.name, "_on: ", p_on )
        print("    ", self.name, "_safety1: ", p_safety1 )
        print("    ", self.name, "_safety2: ", p_safety2 )

        if p_on==GPIO.LOW and p_safety1==GPIO.HIGH and p_safety2==GPIO.HIGH:
            GPIO.output( self.LED_green, GPIO.LOW )
            GPIO.output( self.LED_red, GPIO.HIGH )
        else:
            GPIO.output( self.LED_green, GPIO.HIGH )
            GPIO.output( self.LED_red, GPIO.LOW )



import RPi.GPIO as GPIO
from time import sleep

# Define that we are using physical pin numbers
GPIO.setmode(GPIO.BOARD)

# Create 2 WireCutter Objects
# The constructors for each object will initialize each to its completely OFF state
WC1 = WireCutter( "WC1", 16, 11, 12, 31, 32, 33 )
WC2 = WireCutter( "WC2", 18, 13, 15, 31, 32, 33 )


# Initialize the GPIO pins for LEDs
GPIO.setup( WC1.LED_red, GPIO.OUT, initial=GPIO.HIGH )
GPIO.setup( WC1.LED_green, GPIO.OUT, initial=GPIO.HIGH )
GPIO.setup( WC1.LED_yellow, GPIO.OUT, initial=GPIO.HIGH )


x = input("Run combination tests? <1,0>")
if x == "1":
    # Test all input combinations of WC1
    #   set_state( on, safety1, safety2 )
    WC1.set_state_wait( GPIO.LOW, GPIO.LOW, GPIO.LOW )
    WC1.set_state_wait( GPIO.LOW, GPIO.HIGH, GPIO.LOW )
    WC1.set_state_wait( GPIO.LOW, GPIO.HIGH, GPIO.HIGH )
    # Return to OFF state
    WC1.set_state_wait( GPIO.HIGH, GPIO.LOW, GPIO.LOW )


    # Test wire_cutter circuit 2
    #   set_state_wait( on, safety1, safety2 )
    WC2.set_state_wait( GPIO.LOW, GPIO.LOW, GPIO.LOW )
    WC2.set_state_wait( GPIO.LOW, GPIO.HIGH, GPIO.LOW )
    WC2.set_state_wait( GPIO.LOW, GPIO.HIGH, GPIO.HIGH )
    # Return to OFF state
    WC2.set_state_wait( GPIO.HIGH, GPIO.LOW, GPIO.LOW )

x = input("Run timed tests? <1,0>")
if x == "1":
    # Turn on WC1 in succession 10 times
    for i in range(1,3):
        WC1.set_state( GPIO.LOW, GPIO.HIGH, GPIO.HIGH )
        sleep(i*2)
        WC1.set_state( GPIO.HIGH, GPIO.LOW, GPIO.LOW )
        input( str(i*2) + " second test complete. Press <ENTER> to continue")
        


    # Turn on WC2 in succession 10 times
    for j in range(1,3):
        WC2.set_state( GPIO.LOW, GPIO.HIGH, GPIO.HIGH )
        sleep(j*2)
        WC2.set_state( GPIO.HIGH, GPIO.LOW, GPIO.LOW )
        input( str(j*2) + " second test complete. Press <ENTER> to continue")

# cleanup and end program
input("All tests completed. Exiting program. Press <ENTER> to quit." )
GPIO.cleanup()


