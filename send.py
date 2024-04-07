import board
import busio
import digitalio
import time
#radio
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.RFM69_CS)
reset = digitalio.DigitalInOut(board.RFM69_RST)
import adafruit_rfm69
rfm69 = adafruit_rfm69.RFM69(spi, cs, reset, 915.0)
#buttons
from digitalio import DigitalInOut, Direction, Pull
#potentiometer
from analogio import AnalogIn
from adafruit_simplemath import map_range

#switch
switch = DigitalInOut(board.D10)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

#buttons
button1 = DigitalInOut(board.D12)
button1.direction = Direction.INPUT
button1.pull = Pull.UP

button2 = DigitalInOut(board.D11)
button2.direction = Direction.INPUT
button2.pull = Pull.UP


#potentiometer
analog_in = AnalogIn(board.A1)
def get_voltage(pin):
    return (pin.value * 3.3) / 65536

#what gets sent to the other end
def payload(code, brightness):
    combined_values = code + "," + brightness
    print(combined_values)
    rfm69.send(combined_values)
    time.sleep(.5)


print("Started!")
while True:
    
    #potentiometer 
    #converts the mapped reading to a value between 0 and 1, limite to 2 decimal places
    #adjust the first two number arguments to reflect the max and min of the potentiometer reading
    #if this becomes problematic, you can always just hard code a value
    adjusted_potentiometer_reading = str(round(map_range(get_voltage(analog_in), 0, .4, 0, 1),2))
    print(adjusted_potentiometer_reading)

    if switch.value == True:
        print("true")
        if button1.value == True:
            print("off1")
        if button1.value == False:
            payload("B1", adjusted_potentiometer_reading)
            # print("on1")
            # rfm69.send('B1 hello')
            # #cut this after testing -  just so you can see
            # time.sleep(.5)
        if button2.value == True:
            print("off2")
        if button2.value == False:
            payload("B2", adjusted_potentiometer_reading)
            # print("on2")
            # rfm69.send('B2 hello')
            # #cut this after testing -  just so you can see
            # time.sleep(.5)

    elif switch.value == False:
        print("false")
        if button1.value == True:
            print("off3")
        if button1.value == False:
            payload("B3", adjusted_potentiometer_reading)
            # print("on3")
            # rfm69.send('B3 hello')
            # #cut this after testing -  just so you can see
            # time.sleep(.5)
        if button2.value == True:
            print("off4")
        if button2.value == False:
            payload("B4", adjusted_potentiometer_reading)
            # print("on4")
            # rfm69.send('B4 hello')
            # #cut this after testing -  just so you can see
            # time.sleep(.5)

    #else:
        #print("broken")
    #time.sleep(0.01)
    time.sleep(.5)
