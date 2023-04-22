from machine import Pin, Timer
from utime import sleep

sw1 = Pin(1, Pin.IN, Pin.PULL_UP)
l1 = Pin(4, Pin.OUT)

sw2 = Pin(2, Pin.IN, Pin.PULL_UP)
l2 = Pin(5, Pin.OUT)

sw3 = Pin(3, Pin.IN, Pin.PULL_UP)
l3 = Pin(6, Pin.OUT)

periodo = 1000
led = Pin(7,Pin.OUT)
led_timer = Timer()

while True:
    
    if sw1.value()==0 and sw2.value()==1 and sw3.value()==1:
        print("Tanque 1 vacio, tanque 2 lleno, tanque 3 lleno")
        sleep(1)
        l1.value(1)
        sleep(3)
        print("Tanque lleno")
        l1.value(0)

    if sw1.value()==1 and sw2.value()==0 and sw3.value()==1:
        print("Tanque 1 lleno, tanque 2 vacio, tanque 3 lleno")
        l1.value(0)
        sleep(2)
        print("Llenando tanque 2")
        l2.value(1)
        sleep(3)
        print("Apagando")
        l2.value(0)

    if sw1.value()==1 and sw2.value()==1 and sw3.value()==0:
        print("Tanque 1 lleno, tanque 2 lleno, tanque 3 vacio")
        l1.value(0)
        sleep(2)
        print("Llenando tanque 3")
        l3.value(1)
        sleep(3)
        print("Apagando")
        l3.value(0)

    if sw1.value()==1 and sw2.value()==0 and sw3.value()==0:
        print("Tanque 1 lleno, tanque 2 vacio, tanque 3 vacio")
        l1.value(0)
        sleep(2)
        print("Llenando tanque 2")
        l2.value(1)
        sleep(3)
        l2.value(0)
        print("Llenando tanque 3")
        l3.value(1)
        sleep(3)
        print("Apagando")
        l3.value(0)
    
    if sw1.value()==0 and sw2.value()==1 and sw3.value()==0:
        print("Tanque 1 vacio, tanque 2 lleno, tanque 3 vacio")
        l2.value(0)
        sleep(2)
        print("Llenando tanque 1")
        l1.value(1)
        sleep(3)
        l1.value(0)
        print("Llenando tanque 3")
        l3.value(1)
        sleep(3)
        print("Apagando")
        l3.value(0)

    if sw1.value()==0 and sw2.value()==0 and sw3.value()==1:
        print("Tanque 1 vacio, tanque 2 vacio, tanque 3 lleno")
        l3.value(0)
        sleep(2)
        print("Llenando tanque 1")
        l1.value(1)
        sleep(3)
        l1.value(0)
        print("Llenando tanque 2")
        l2.value(1)
        sleep(3)
        print("Apagando")
        l2.value(0)
        
    if sw1.value()==0 and sw2.value()==0 and sw3.value()==0:
        print("Tanque 1 vacio, tanque 2 vacio, tanque 3 vacio")
        l1.value(0)
        sleep(2)
        print("Llenando tanque 1")
        l1.value(1)
        sleep(3)
        l1.value(0)
        print("Llenando tanque 2")
        l2.value(1)
        sleep(3)
        l2.value(0)
        print("Llenando tanque 3")
        l3.value(1)
        sleep(3)
        print("Apagando")
        l3.value(0)
        

        