from machine import Pin,Timer
#import time

led = machine.Pin(25,machine.Pin.OUT)
zaman = Timer()

def tersle(biling):
    led.toggle()
    
zaman.init(freq=2,mode=Timer.PERIODIC,callback=tersle)    


    