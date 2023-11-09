from dfplayermini import Player
from time import sleep

#Rx-Tx2=17
#Tx-Rx2=16

music = Player(pin_TX=17, pin_RX=16)

music.play(1)
sleep(30)
music.play(3)
sleep(30)
music.play(2)
sleep(30)
music.play(2)
sleep(30)
music.play(3)
sleep(30)
music.play(2)

music.module_sleep()

