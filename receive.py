import board
import busio
import digitalio
import analogio
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

cs = digitalio.DigitalInOut(board.RFM69_CS)
reset = digitalio.DigitalInOut(board.RFM69_RST)

import adafruit_rfm69
rfm69 = adafruit_rfm69.RFM69(spi, cs, reset, 915.0)

#for measuring power
vbat_voltage = analogio.AnalogIn(board.D9)

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
YELLOW = (255,255,0)
PURPLE = (0,255,255)
BLACK = (0,0,0)

#original startup
# color_state = BLUE
# pixels.fill(color_state)
# pixels[2] = RED
# pixels.show()

#get voltage
def get_voltage(pin):
    return (pin.value * 3.3 / 65536 * 2)
battery_voltage = get_voltage(vbat_voltage)
print("vbat voltage: ")
print(battery_voltage)

#illuminate lights at startup to show voltage
#according to the site below, "LiPoly batteries are 'maxed out' at 4.2V and stick around 3.7V for much of the battery life, then slowly sink down to 3.2V or so before the protection circuitry cuts it off. By measuring the voltage you can quickly tell when you're heading below 3.7V."
#https://learn.adafruit.com/adafruit-feather-m0-radio-with-rfm69-packet-radio/power-management

#move the red dot according to what the voltage is
pixels.fill(BLUE)
if battery_voltage > 4.1:
    pixels[7] = RED
elif battery_voltage > 4:
    pixels[6] = RED
elif battery_voltage > 3.9:
    pixels[5] = RED
elif battery_voltage > 3.7:
    pixels[4] = RED
elif battery_voltage > 3.6:
    pixels[3] = RED
elif battery_voltage > 3.3:
    pixels[2] = RED
elif battery_voltage > 3.1:
    pixels[1] = RED
else:
    pixels[0] = RED


pixels.show()


def update_lights(color, brightness_level):
    pixel.deinit()
    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness_level, auto_write=False, pixel_order=ORDER)

while True:


    packet = rfm69.receive()  # Wait for a packet to be received (up to 0.5 seconds)
    if packet is not None:
        packet_text = str(packet, 'ascii')
        print('Received: {0}'.format(packet_text))

        #parse the payload
        split_payload = packet_text.split(",")
        print(split_payload[0])
        payload_code = split_payload[0]
        brightness_value = split_payload[1]
        #not sure why you need to use eval to covert this into an int, but it works
        brightness_value_int = eval(brightness_value)
        print(brightness_value)
        

        #reset the brightness
        pixels.deinit()
        pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness_value_int, auto_write=False, pixel_order=ORDER)

        if payload_code == 'B5':
            print('lights are off')
            color_state = BLACK
        if payload_code == 'B6':
            color_state = GREEN
            print('we have green lights')
        if payload_code == 'B7':
            color_state = YELLOW
            print('we have yellow lights')
        if payload_code == 'B8':
            color_state = RED
            print('we have red lights')
        pixels.fill(color_state)
        pixels.show()
