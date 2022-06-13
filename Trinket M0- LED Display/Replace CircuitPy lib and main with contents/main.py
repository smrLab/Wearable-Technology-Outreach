# SMRL Outreach Flexible Circuit LED Display
#   for Trinket M0, CircuitPython ver. 7.3.0
# by Eric Markvicka, Soft Materials and Robotics Laboratory, UNL
# 6/7/22

import board
import digitalio
import time
import random

## initialize LEDs
# pin 13, built-in red LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# digital I/O pins
led_0 = digitalio.DigitalInOut(board.D0)
led_0.direction = digitalio.Direction.OUTPUT

led_1 = digitalio.DigitalInOut(board.D1)
led_1.direction = digitalio.Direction.OUTPUT

led_2 = digitalio.DigitalInOut(board.D2)
led_2.direction = digitalio.Direction.OUTPUT

led_3 = digitalio.DigitalInOut(board.D3)
led_3.direction = digitalio.Direction.OUTPUT

led_4 = digitalio.DigitalInOut(board.D4)
led_4.direction = digitalio.Direction.OUTPUT

while True:
    ##################################################
    # One ON LED and all other OFF
    ##################################################
    list = [led_0, led_1, led_2, led_3, led_4]

    # turn all LEDs OFF
    for i in list:
        i.value = False

    for i in range(20):
        # random value from 0 to 4
        idx = random.choice(range(5))

        list[idx].value = True # turn LED ON

        time.sleep(0.5) # delay

        list[idx].value = False # turn LED OFF

    ##################################################
    # One OFF LED and all other ON
    ##################################################
    list = [led_0, led_1, led_2, led_3, led_4]

    # turn all LEDs ON
    for i in list:
        i.value = True

    for i in range(20):
        # random value from 0 to 4
        idx = random.choice(range(5))

        list[idx].value = False # turn LED OFF

        time.sleep(0.5) # delay

        list[idx].value = True # turn LED ON

    ##################################################
    # Turning all LEDs ON/OFF one by one in a stack
    ##################################################
    list = [led_0, led_1, led_2, led_3, led_4]

    for j in range(4):
        # turn all LEDs ON
        for i in list:
            i.value = True # turn LED ON
            time.sleep(0.5) # delay

        for i in list:
            i.value = False # turn LED OFF
            time.sleep(0.5) # delay


    ##################################################
    # LED chase- two ON
    ##################################################
    list = [led_0, led_1, led_2, led_3, led_4]

    for j in range(4):
        prev_led_1 = led_0
        prev_led_2 = led_4

        for i in range(4):
            list[i+1].value = True # turn LED ON
            prev_led_1.value = True # turn prev LED ON
            prev_led_2.value = False # turn prev_2 LED OFF
            time.sleep(0.5) # delay

            # update vars
            prev_led_1 = list[i+1]
            prev_led_2 = prev_led_1

        # finish chase
        led_4.value = True # turn prev LED ON
        led_1.value = True # turn prev LED ON
        led_3.value = False # turn prev_2 LED OFF
        time.sleep(0.5) # delay
