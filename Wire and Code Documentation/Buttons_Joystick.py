import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import spidev
import time
import os

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

DEBUG = False

GPIO.setwarnings(False) # Ignore warning for now

GPIO.setmode(GPIO.BCM) # Use the Broadcom pin mode

buttons = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 17, 16, 13]
# what they mean L to R
# right side:
# 18, 19, 20, 21, 22, 23 = A, B, X, Y, Bumper, Trigger
# Left side:
# 24, 25, 26, 27, 12, 16 = D arrow, L arrow, R arrow, U arrow, Bumper, Trigger
# Extra:
# 13 = ESC button

GPIO.setup(buttons, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set buttons to auto-down


# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data


# Define sensor channels
# (channels 6 to 7 unused)
swt_channel = 0
vrx_channel = 1
vry_channel = 2
swt2_channel = 3
vrx2_channel = 4
vry2_channel = 5

# Define delay between readings (s)
delay = 0.5


def rightJoystick():
    # Read the first joystick position data
    vrx_pos = ReadChannel(vrx_channel)
    vry_pos = ReadChannel(vry_channel)
    # Read switch state
    swt_val = ReadChannel(swt_channel)
    return vrx_pos, vry_pos, swt_val # Return x,y,and pressed postion

def leftJoystick():
    # Read the second joystick position data
    vrx2_pos = ReadChannel(vrx_channel)
    vry2_pos = ReadChannel(vry_channel)
    # Read switch state
    swt2_val = ReadChannel(swt_channel)
    return vrx2_pos, vry2_pos, swt2_val  # Return x,y,and pressed postion

while True:
    x1, y1, b1 =rightJoystick() # get right joystick
    x2, y2, b2 =leftJoystick() # get left Joystick
    for i in range(len(buttons)): # get other buttons
        if (GPIO.input(buttons[i]) == True):
            print (i)
    print ("Right joystick = x: {} y: {} b: {}".format(x1,y1,b1))
    print ("Left joystick  = x: {} y: {} b: {}".format(x2,y2,b2))
    
    sleep(delay)