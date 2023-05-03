from machine import Pin, SoftSPI, I2C
import utime 
import dht
from ssd1306 import SSD1306_I2C

ANCHO=128
ALTO=64

sensor = dht.DHT11(Pin(0))

i2c=I2C(0,scl=Pin(17),sda=Pin(16))
oled=SSD1306_I2C(ANCHO,ALTO,i2c)

while True:
  oled.fill(0)
  try:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()

    ftemp = float(temp)
    fhum = float(hum)
    stemp = str(ftemp)
    shum = str(fhum)

    print('Temperature: %3.1f C' %temp)
    print('Humedad: %3.1f C' %hum)
    print('')


    oled.text("Lec. Sensor:", 0, 0)
    oled.text("Temp: ", 0, 15)
    oled.text(stemp, 50, 15)
    oled.text("Hum: ", 0, 25)
    oled.text(shum, 50, 25)
    oled.show()



    utime.sleep(5)


    
  except OSError as e:
    print('Failed to read sensor.')