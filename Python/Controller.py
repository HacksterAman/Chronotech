from machine import Pin
from time import sleep

# Left Stepper motor
in1 = Pin(32,Pin.OUT)
in2 = Pin(33,Pin.OUT)
in3 = Pin(25,Pin.OUT)
in4 = Pin(26,Pin.OUT)

# Right Stepper motor
In1 = Pin(13,Pin.OUT)
In2 = Pin(12,Pin.OUT)
In3 = Pin(14,Pin.OUT)
In4 = Pin(27,Pin.OUT)

sequence = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

def stepper(motor,count):
    for x in range(abs(count)):
        for step in sequence[::(2*(count>0)-1)]:
            for i in range(4):
                motor[i].value(step[i])
                sleep(0.001)
    for i in range(4):
        motor[i].value(0)

def move(steps,m):
    motor=[in1,in2,in3,in4] if m==-1 else [In1,In2,In3,In4]
    for i in steps:
        stepper(motor,i)
    print("Rotation Done for Motor",m)
