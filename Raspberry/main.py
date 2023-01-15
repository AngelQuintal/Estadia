from machine import Pin, UART

pin = Pin(2, Pin.OUT)

while True:
    pin.write(1)
    