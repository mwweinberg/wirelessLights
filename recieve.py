import board
import busio
import digitalio
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

cs = digitalio.DigitalInOut(board.RFM69_CS)
reset = digitalio.DigitalInOut(board.RFM69_RST)

import adafruit_rfm69
rfm69 = adafruit_rfm69.RFM69(spi, cs, reset, 915.0)


#for pixels
import time
import neopixel

pixel_pin = board.A1
num_pixels = 8
#use GRBW for the sticks, RGB for the circle
ORDER = neopixel.GRBW
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False, pixel_order=ORDER)

RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)


pixels.fill(BLUE)
pixels.show()
while True:


    packet = rfm69.receive()  # Wait for a packet to be received (up to 0.5 seconds)
    if packet is not None:
        packet_text = str(packet, 'ascii')
        print('Received: {0}'.format(packet_text))
        if packet_text == 'B1 hello':
            print('we have green lights')
            pixels.fill(GREEN)
        if packet_text == 'B2 hello':
            pixels.fill(RED)
            print('we have red lights')
        pixels.show()
