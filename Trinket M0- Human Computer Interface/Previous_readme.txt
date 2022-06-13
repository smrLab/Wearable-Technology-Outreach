SMRL Outreach Capacitive Touch Sleeve - Deployment Guide
Kasey Moomau, 6/2/22

This readme summarizes the steps you will need from these tutorials on Adafruit:
https://learn.adafruit.com/adafruit-mpr121-12-key-capacitive-touch-sensor-breakout-tutorial
https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/overview

In this package there are two folders, one containing the CircuitPython 'OS' (a .UF2 file), 
	and one containing the code (a 'lib' folder and a 'main.py' file).

--- Updating circuitpython version on each trinket:  ---
1. Hook each new trinket M0 up to a computer with a known-good data cable, and double-tap the 
	button on the end to bring up the bootloader (you'll see files with .UF2 extensions.
2. Navigate up one level, until you see the TRINKETBOOT icon. 
3. Drag the .UF2 file out of the "Update CircuitPy version..." folder onto TRINKETBOOT.
	The Trinket will restart, loading the new version.

--- Loading code onto each trinket: ---
4. Once the Trinket has reset, copy the 'lib' folder and main.py file from 
	the "Replace CircuitPy lib..." folder into the CIRCUITPY folder (This will look like a
	USB drive, and may open automatically when the board resets).

--- Plug in the MPR121 ---
5. Insert a Stemma QT four-wire connector into the MPR121 at either end.
6. Plug the black jumper wire onto the GND pin on the Trinket.
7. Plug the red jumper wire onto the 3V pin on the Trinket.
8. Plug the blue jumper wire on to the 0 pin on the Trinket. (This is SDA for the I2C)
9. Plug the yellow jumper wire onto the 2 pin on the Trinket. (This is the SCL for the I2C)

--- Verify ---
10. Place the cursor of your device (that the Trinket USB is plugged into) into a text field,
	and touch the pads on the MPR121. Variations on the letters 'W', 'A', 'S', and 'D' should
	appear in the text field. You may customize these in the Keys_Pressed list in 'main.py'.