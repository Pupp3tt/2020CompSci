# Name: Matthew Tucker
# Date: 5/6/2020
# Discription: Take in all inputs and use other code to determin what to do


import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import spidev # import spidec (code for 3008 chip)
import time
import os
import Output_Functions

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz =1000000

DEBUG = False

GPIO.setwarnings(False) # Ignore warning for now

GPIO.setmode(GPIO.BCM) # Use the Broadcom pin mode

buttons = [19, 20, 23, 13, 16, 17, 26]
# all avalible buttons:
# 18, 19, 20, 21, 22, 23
# 24, 25, 26, 27, 12, 16
# 13

# used and what they do buttons:
# 19: change wepons + 1
# 20: jump
# 23: shoot
# 13: use items
# 16: change wepons -1
# 17: ESC/Pause
# 26: spawn 1 zombie


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
    vrx2_pos = ReadChannel(vrx2_channel)
    vry2_pos = ReadChannel(vry2_channel)
    # Read switch state
    swt2_val = ReadChannel(swt2_channel)
    return vrx2_pos, vry2_pos, swt2_val  # Return x,y,and pressed postion

def checkButtons(i): # check right buttons based off the index in list
    if (i == 0): # +1 on wepons
        return "wepon"
    if (i == 1): # jump
        return "jump"
    if (i == 2): # shoot
        return "shoot"
    if (i == 3): # use items
        return "item"
    if (i == 4): # -1 on wepons
        return "wepons"
    if (i == 5): #ESC
        return "ESC"
    if (i == 6): #spawn zombie
        return "zombie"

def movePlayer(): # check right joystick x value
    # check for x
    x = ReadChannel(vrx_channel)
    #print ("x value")
    #print (x)
    if (10 <= x <= 1000):
        return "stand"
    else:
        if(x >= 1000):
            return "right"
        elif(x<= 10):
            return "left"

def moveCrossHair(): # check left joystick x and y value
    # Check for x
    x, y, s = leftJoystick()
    if (x >= 1000):
        print ("Left")
    elif (x <= 10):
        print ("Right")
    else:
        pass
    # Check for y
    if (y >= 1000):
        print ("up")
    elif (y <= 10):
        print ("down")
    else:
        pass

def checkAll(): # a function to do everything
    for i in range(len(buttons)):  # Check all buttons
        if (GPIO.input(buttons[i]) == True):  # If one is press find that button #
            first = checkButtons(i)  # do something with buttons #

    # joystick right
    second = movePlayer()
    # joystick left
    # moveCrossHair()
    # sleep
    time.sleep(0.1)
    # return code
    return first, second





       # Actual Code for testing
#while True:
    #checkAll()
       # Check all inputs and do what need to happen