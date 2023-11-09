import time, _thread
from Rotation import step
from Controller import move
(h,m)=(0,0)
while True:
    t=time.localtime()
    (new_h,new_m)=(t[3],t[4])
    if m!=new_m:
        m=new_m
        _thread.start_new_thread(move(step(m, 1),1))
        if h!=new_h:
            h=new_h
            _thread.start_new_thread(move(step(h,-1),-1))
        print(h,':',m)
    time.sleep(1)