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
# 18, 19, 20, 21, 22, 23
# Left side:
# 24, 25, 26, 27, 12, 16
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

def checkRight(i): # check right buttons based off the index in list
    if (i == 0):
        print ("Yellow") # up
    if (i == 1):
        print ("Gray") # bumper
    if (i == 2):
        print ("Green") # down
    if (i == 3):
        print ("Blue") # left
    if (i == 4):
        print ("Red") # Right
    if (i == 5):
        print ("White") # Triger

def checkLeft(i): # check left buttons based off the index in list
    if (i == 6):
        print ("Yellow")
    if (i == 7):
        print ("Gray")
    if (i == 8):
        print ("Green")
    if (i == 9):
        print ("Blue")
    if (i == 10):
        print ("Red")
    if (i == 11):
        print ("White")

def movePlayer(x): # check right joystick x value
    # check for x
    if(x >= 1000):
        print ("left")
    elif(x<= 10):
        print ("Right")
    else:
        pass

def moveCrossHair(x,y): # check left joystick x and y value
    # Check for x
    if (x >= 1000):
        print ("right")
    elif (x <= 10):
        print ("left")
    else:
        pass
    # Check for y
    if (y >= 1000):
        print ("up")
    elif (y <= 10):
        print ("down")
    else:
        pass

while True:
    for i in range(len(buttons)):# Check all buttons
        if (GPIO.input(buttons[i]) == True): # If one is press find that button
            if (i == 12): # If ESC then do this
                print ("black")

            checkRight(i) # If on right then do that
            checkLeft(i) # If on left the do that

    vrx_pos, vry_pos, swt_val = rightJoystick()
    vrx2_pos, vry2_pos, swt2_val = leftJoystick()
    # joystick right
    movePlayer(vrx_pos)
    moveCrossHair(vrx2_pos,vry2_pos)