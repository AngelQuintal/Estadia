from machine import Pin, ADC, I2C
from utime import sleep
from ssd1306 import SSD1306_I2C

ANCHO=128
ALTO=64

pot = ADC(0)
factor_16 = 3.3 / (65535)

i2c=I2C(0,scl=Pin(1),sda=Pin(0))
oled=SSD1306_I2C(ANCHO,ALTO,i2c)

while True:
    oled.fill(0)
    
    pot_leer = pot.read_u16() * factor_16
    
    spot_leer = str(pot_leer)
    
    print(pot_leer)
    
    oled.text("ADC Valor", 0, 0)
    oled.text("ADC: ", 0, 15)
    oled.text(spot_leer, 35, 15)
    oled.show()
    
    sleep(2)