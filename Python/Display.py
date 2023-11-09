from machine import Pin, SPI
import max7219, _thread, time
from time import sleep,sleep_ms
from font_4x6 import font_4x6
from font_6x8 import font_6x8

#DIN-D2=2
#CS-D5=5
#CLK-D4=4

spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(4), mosi=Pin(2))
cs = Pin(5, Pin.OUT)

display = max7219.Matrix8x8(spi, cs, 4)
display.brightness(10)

class clock_display:
    def __init__(self,x,y,size):
        self.x=x
        self.y=y
        self.size=size
        self.prev_text='--'
        if self.size=='small':
            self.font=font_4x6
            self.a=4
            self.b=6
            self.byte=0x20
        elif self.size=='big':
            self.font=font_6x8
            self.a=6
            self.b=8
            self.byte=0x80        

    def show_num(self,num):
        text=str(num)
        if num<10:text='0'+text
        if text!=self.prev_text:
            self.scroll_down(text)
            self.prev_text=text
                
    def scroll_down(self,text):
        for y in range(self.y-8, self.y+1):  
            self.put_text(text,self.x,y)
            self.put_text(self.prev_text,self.x,y+8)   
            display.show()
            sleep(0.05)
            
    def put_text(self,text,x,y):
        for uchr in text:
            sym = self.font[ord(uchr)]
            for i in range(self.a):
                for j in range(self.b):
                    display.pixel(x + i, y + j, 1 if sym[i] & (self.byte >> j) else 0)
            x += self.a
        display.show()
        
def separator(mode):
    for y in [1,2,4,5]:
        display.pixel(11, y,mode)
        display.show()
            
display.fill(0)
display.show()
sleep_ms(250)

H=clock_display(0, -1, 'big')
M=clock_display(13, -1, 'big')
S=clock_display(25, 2, 'small')

s=0
def clock():
    while True:
        t=time.localtime()
        if s!=t[5]:
            s=t[5]
            separator(s%2)
            S.show_num(s)
            M.show_num(t[4])
            H.show_num(t[3])

clock()
        