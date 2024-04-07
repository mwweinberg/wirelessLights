#To flash circuit python onto a board
The folder bossac-1.7.0 has both the flasher and the special version of circuitpython that works with the board. Open that folder in terminal and type 

./bossac -p /dev/ttyACM0 -e -w -v -R adafruit-circuitpython-feather_m0_rfm69-en_US-9.0.3.bin 

this command runs bossac (the flasher) targeted the board (/dev/ttyAMC0) and loads the version of circuitpython in the folder.  If for some reason you get an error about the board port, run ls /dev/ for a list of boards. There should be a ttyACM0, but maybe it is ttyACM1 or something? 


#/basic_board_exchange_scripts?

This folder has a simple send/recieve script pair that works.  If everything breaks you can always roll back to them.

