# Complete project details at https://RandomNerdTutorials.com

import socket

import network, time, Server, _thread, ntptime

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Aman197'
password = 'ushaaman'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

_thread.start_new_thread(Server.host_server,())

#(year, month, mday, week_of_year, hour, minute, second, milisecond)
offset=19800
print("Local time before synchronization：%s" %str(time.localtime(time.time()+offset)))
ntptime.settime()
print("Local time after synchronization：%s" %str(time.localtime(time.time()+offset)))