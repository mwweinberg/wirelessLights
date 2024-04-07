import board
import busio
import digitalio
#radio
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.RFM69_CS)
reset = digitalio.DigitalInOut(board.RFM69_RST)
#buttons
from digitalio import DigitalInOut, Direction, Pull

import adafruit_rfm69
rfm69 = adafruit_rfm69.RFM69(spi, cs, reset, 915.0)


#just for testing
import time

#buttons
button1 = DigitalInOut(board.D12)
button1.direction = Direction.INPUT
button1.pull = Pull.UP

button2 = DigitalInOut(board.D11)
button2.direction = Direction.INPUT 
button2.pull = Pull.UP 

print("Started!")
while True:
    #print("Hello, CircuitPython!")
    #rfm69.send('Hello world!')
    #time.sleep(2)
    if button1.value == True:
        print("off1")
    if button1.value == False:
       print("on1")
       rfm69.send('B1 hello')
       #cut this after testing -  just so you can see
       time.sleep(.5)
    if button2.value == True:
        print("off2")
    if button2.value == False:
       print("on2")
       rfm69.send('B2 hello')
       #cut this after testing -  just so you can see
       time.sleep(.5)
    
    
    
    #else:
        #print("broken")
    time.sleep(0.01)
