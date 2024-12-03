' ME473 lab1.py basic example for reading and writing voltages, 9/25/2024'

# to run this code, first copy pyboard.py into the same directory as this file. 
# then run this program as follows: 
# windows: find which COM port, e.g. COM16, by going to device manager->Ports
#    python pyboard.py --device COM<x> lab1.py 
# Mac: 
#    python pyboard.py --device /dev/tty.usbmodem* lab1.py
# Linux: (if this won't work and you're running linux, figure it out yourself)
#    python pyboard.py --device /dev/ttyUSB2 lab1.py


import time, board 
import math # example usage: math.sin(x), math.sqrt(x), math.pi
from analogio import AnalogOut, AnalogIn
import adafruit_dotstar                     # driver for color LED      

###################################################
# hardware configuration and helper functions
Vfs = 3.3                                   # volts, the full-scale output range
A0_pin = AnalogOut(board.A0)                # configure pin for output
A1_pin = AnalogOut(board.A1)                # configure pin for output
A2_pin = AnalogIn(board.A2)                 # configure pin for input
A3_pin = AnalogIn(board.A3)                 # configure pin for input
led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)

def get_voltage(pin):
    return pin.value / 65536 * Vfs

def set_voltage(pin, voltage):
    pin.value = int(voltage/Vfs * 65535)  # pin.value must be an int
    return voltage

###################################################
# parameters
Tfinal = 1                                  # [s] length of time to run
Ts = 0.1                                    # [s] *approximate* sample period

###################################################
# run the experiment!
t0_ns = time.monotonic_ns() # [ns] time measured in nanoseconds
while True: # infinite loop until break statement
    t = (time.monotonic_ns() - t0_ns) * 10**-9
    
    # check if it's time to stop; break out of infinite loop if it is
    if t > Tfinal: break
    
    # send out voltage
    A0_V = set_voltage(A0_pin, 1)

    # read voltage
    A2_V = get_voltage(A2_pin)
    A3_V = get_voltage(A3_pin)

    # set LED brightness proportional to output voltage
    led[0] = (int(A0_V/Vfs * 50), 0, int(A0_V/Vfs * 255))
    
    print('%2.4f %1.3f %1.3f  %1.3f'%(t, A0_V, A2_V, A3_V))
    
    time.sleep(Ts - 0.002)