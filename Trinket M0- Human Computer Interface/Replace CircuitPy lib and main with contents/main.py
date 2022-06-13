# SMRL Outreach Flexible Circuit Capacitive Touch Controller
#   for Trinket M0, CircuitPython ver. 7.3.0
# by Kasey Moomau and Eric Markvicka, Soft Materials and Robotics Laboratory, UNL
# 6/9/22

import time
import board
import busio
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import adafruit_mpr121


## Setup

# Set loop duration in seconds
print("Hello, world!")
loopDuration = 0.1

##################################
# Choose keys for pads 0-11 on the MPR121
# other options include Keycode.DOWN_ARROW, Keycode.UP_ARROW, etc, see link below.
#   https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html
# These entries can be changed to emulate whatever keys desired,
# Using any pad 0-11 on the MPR121, duplicates are okay.
key_pressed = []
key_pressed.append(Keycode.D)  # pin 0
key_pressed.append(Keycode.W)  # pin 1
key_pressed.append(Keycode.S)  # pin 2
key_pressed.append(Keycode.A)  # pin 3

key_pressed.append(Keycode.D)  # pin 4  **RIGHT** (D)
key_pressed.append(Keycode.S)  # pin 5  **DOWN** (S)
key_pressed.append(Keycode.A)  # pin 6  **LEFT (A)
key_pressed.append(Keycode.W)  # pin 7  **UP** (W)

key_pressed.append(Keycode.D)  # pin 8
key_pressed.append(Keycode.W)  # pin 9
key_pressed.append(Keycode.S)  # pin 10
key_pressed.append(Keycode.A)  # pin 11


################# LEDs #################
led1 = digitalio.DigitalInOut(board.D1)
led1.direction = digitalio.Direction.OUTPUT

led3 = digitalio.DigitalInOut(board.D3)
led3.direction = digitalio.Direction.OUTPUT

led4 = digitalio.DigitalInOut(board.D4)
led4.direction = digitalio.Direction.OUTPUT

## built-in red LED
led13 = digitalio.DigitalInOut(board.D13)
led13.direction = digitalio.Direction.OUTPUT

## list of LEDs
ledList = [led1, led3, led4, led13]

# The keyboard object!
time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)

# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Create MPR121 object.
mpr121 = adafruit_mpr121.MPR121(i2c)

# Loop forever testing each input pad on the MPR121 and
# outputting keypresses and lighting LEDs when pads are touched.
while True:

    # Loop through all 12 inputs (0-11).
    for i in range(12):
        # Call is_touched and pass it then number of the input.  If it's touched
        # it will return True, otherwise it will return False.
        if mpr121[i].value:
            # uncomment line below for touch info in REPL
            # print("Input {} touched!".format(i))
            keyboard.press(key_pressed[i])  # "Press"...
            keyboard.release_all()  # ..."Release"!

            # Turn on up LED if up pad is pressed
            if i == 7: # if pad 7 is pressed
                led1.value = True  # turn on the top LED (pin 1)
            # Turn on right LED if right pad is pressed
            if i == 4: # if pad 4 is pressed
                led3.value = True  # turn on the right LED (pin 3)
            # Turn on left LED if left pad is pressed
            if i == 6: # if pad 6 is pressed
                led13.value = True  # turn on the left (built-in) LED (pin 13)
            # Turn on down LED if down pad is pressed
            if i == 5: # if pad 5 is pressed
                led4.value = True  # turn on the bottom LED (pin 4)


    time.sleep(loopDuration)  # Small delay to keep from spamming output messages.

    # turn off all LEDs at end of loop to reset
    for i in ledList: #cycle through all four LEDs in the list
        i.value = False #turn off the i-th LED in the list
