from machine import PWM, Pin
import time

enable = Pin(18, Pin.OUT)
left = Pin(0, Pin.OUT)
right = Pin(1, Pin.OUT)

trig = Pin(15, Pin.OUT)
echo = Pin(14, Pin.IN)


#右超信地旋回
def TurnR(msec):
    enable.value(1)
    left.value(1)
    right.value(0)
    print("turn right")
    time.sleep(msec)
    
#左超信地旋回
def TurnL(msec):
    enable.value(1)
    left.value(0)
    right.value(1)
    print("turn left")
    time.sleep(msec)
    
#前進
def Forword(msec):
    enable.value(1)
    left.value(1)
    right.value(1)
    print("forword")
    time.sleep(msec)
    
#停止
def stop(msec):
    enable.value(0)
    print("stop")
    time.sleep(msec)
    
def Back(msec):
    enable.value(1)
    left.value(0)
    right.value(0)
    print("back")
    time.sleep(msec)

servo1 = PWM(Pin(7))
servo1.freq(50)


while True :
    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(10)
    trig.low()
    signaloff, signalon = 0, 0
    while echo.value() == 0:
        signaloff = time.ticks_us()
    while echo.value() == 1:
        signalon = time.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print("dinstance: ",distance,"cm")
    time.sleep(0.1)
    
    if distance <= 10:
        Back(1)
        TurnR(0.5)
        

    else:
        Forword(0.1)
   
    
stop()    
    
        
    