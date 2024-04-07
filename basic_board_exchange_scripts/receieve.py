import board
import busio
import digitalio
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

cs = digitalio.DigitalInOut(board.RFM69_CS)
reset = digitalio.DigitalInOut(board.RFM69_RST)

import adafruit_rfm69
rfm69 = adafruit_rfm69.RFM69(spi, cs, reset, 915.0)


#just for testing
import time

while True:
    #print("Hello, CircuitPython!")
    #rfm69.send('Hello world!')
    
    #time.sleep(2)
    packet = rfm69.receive()  # Wait for a packet to be received (up to 0.5 seconds)
    if packet is not None:
        packet_text = str(packet, 'ascii')
        print('Received: {0}'.format(packet_text))