from dfplayermini import Player

from time import sleep

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
# 
# music.fadeout(2000)
# 
# music.play(2)
# music.loop()
# sleep(20)

music.module_sleep()
