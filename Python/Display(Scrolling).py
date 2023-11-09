from machine import Pin, SPI
import max7219
from time import sleep

#DIN-D2
#CS-D5
#CLK-D4

spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(4), mosi=Pin(2))
cs = Pin(5, Pin.OUT)

display = max7219.Matrix8x8(spi, cs, 4)

display.brightness(10)

scrolling_message = "Hello"
length = len(scrolling_message)
column = (length *8)

display.fill(0)
display.show()
sleep(1)

while True:
    for x in range(32, -column, -1):     
        display.fill(0)
        display.text(scrolling_message ,x,0,1)
        display.show()
        sleep(0.05)
