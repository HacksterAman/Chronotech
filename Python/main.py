print('Started working')

from dfplayermini import Player
from time import sleep, sleep_ms

#Rx-Tx2=17
#Tx-Rx2=16

music = Player(pin_TX=17, pin_RX=16)
sleep(2)
music.play(1)

import Server, Display, _thread
_thread.start_new_thread(Display.display_clock,())

while True:
    output=Server.host_server()
    if output:
        print(output)
        if output==2:
            Display.clock=False
            music.play(2)
            sleep_ms(250)
            for i in range(3):
                Display.display_text("HappyBirthdayToYou!!")
                print("Happy Birthday To You Sir!!")
            Display.clock=True
        elif output==3:
            Display.clock=True
            print("Displaying The Clock")
        elif output==4:
            music.play(3)
            print("Alarm Playing")
        elif output==5:
            music.stop()
            print("Audio Stopped")
        else:
            Display.clock=False
            Display.display_text(output)
            Display.clock=True

