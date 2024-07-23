# Wireless Lights

This is hardware and software to create remote controlled speaker notification lights.  There are two different lights, both of which are controlled from the same controller.  You can toggle which lights you are controlling with a switch on the controller itself.  You can also set the brightness of the lights.

![animated gif of the lights in use](/wirelessLights.gif)

## Controller buttons

### Top row (left to right, controls color of light)

Off, Red, Yellow, Green

### Bottom row (left to right)

Power, toggle which light you are controlling, brightness setting of controlled light 


# Building/editing

You will need to flash the feathers to use circuitpython:

#To flash circuit python onto a board on linux
The folder bossac-1.7.0 has both the flasher and the special version of circuitpython that works with the board. Open that folder in terminal and type 

./bossac -p /dev/ttyACM0 -e -w -v -R adafruit-circuitpython-feather_m0_rfm69-en_US-9.0.3.bin 

this command runs bossac (the flasher) targeted the board (/dev/ttyAMC0) and loads the version of circuitpython in the folder.  If for some reason you get an error about the board port, run ls /dev/ for a list of boards. There should be a ttyACM0, but maybe it is ttyACM1 or something? 

# Code 

send.py is the file for the transmitter
receive.py is the file for the primary receiver (when the transmitter is set to the first position)
receive_alt.py is the file for the second receiver (when the transmitter is set to the second position). The only difference between the two is the B numbers in lines 60-71

you also need to add the /lib files when you are setting up a new board

#/basic_board_exchange_scripts?

This folder has a simple send/recieve script pair that works for testing.  If everything breaks you can always roll back to them.

# Circuit diagrams 

in /fritzing

