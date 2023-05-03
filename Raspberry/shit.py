import os
from machine import Pin, SoftSPI, I2C
import utime 
import dht
from sdcard import SDCard
import _thread
from ssd1306 import SSD1306_I2C

ANCHO=128
ALTO=64

sensor = dht.DHT11(Pin(28))
pin = Pin(12, Pin.IN)

i2c=I2C(0,scl=Pin(14),sda=Pin(15))
oled=SSD1306_I2C(ANCHO,ALTO,i2c)

escribir = False

# Pin assignment:
# MISO -> GPIO 12
# MOSI -> GPIO 11
# SCK  -> GPIO 10
# CS   -> GPIO 13
# VCC  -> 5V
# GND -> GND

spisd = SoftSPI(-1, miso=Pin(12), mosi=Pin(11), sck=Pin(10))
sd = SDCard(spisd, Pin(13))


print('Root directory:{}'.format(os.listdir()))
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')
print('Root directory:{}'.format(os.listdir()))
os.chdir('sd')
print('SD Card contains:{}'.format(os.listdir()))

def sd_interruption(pin):
   global escribir
   escribir = True
   global interup_escribir
   interup_escribir = pin

   temp = sensor.temperature()
   hum = sensor.humidity()

   ftemp = float(temp)
   fhum = float(hum)
   stemp = str(ftemp)
   shum = str(fhum)

   f = open('Temp_test1.txt', 'a')
   f.write("Temperatura: " + stemp + " / " + "Humedad: " + shum + '\n')
   f.close()
   
   utime.sleep(5)


pin.irq(trigger = Pin.IRQ_RISING, handler = sd_interruption)

def sdcard_write ():
    while True:
        
        temp = sensor.temperature()
        hum = sensor.humidity()
        ftemp = float(temp)
        fhum = float(hum)
        stemp = str(ftemp)
        shum = str(fhum)
        
        f.write("Temperatura: " + stemp + " / " + "Humedad: " + shum + '\n')
        f.write(stemp + '\n')
        f.close()
        
        print("Datos escritos")
        
        utime.sleep(5)
_thread.start_new_thread(sdcard_write,())

while True:
  oled.fill(0)
  try:
    sensor.measure()
    temp = sensor.temperature()

    ftemp = float(temp)
    fhum = float(hum)
    stemp = str(ftemp)
    shum = str(fhum)

    print('Temperature: %3.1f C' %temp)
    print('Humedad: %3.1f C' %hum)
    print('')


    oled.text("Lectura de sensor:", 0, 0)
    oled.text("Temp: ", 0, 15)
    oled.text(stemp, 10, 15)
    oled.text("Hum: ", 0, 25)
    oled.text(shum, 10, 25)



    utime.sleep(5)


    
  except OSError as e:
    print('Failed to read sensor.')
