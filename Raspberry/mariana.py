from machine import Pin, I2C
from utime import sleep
from ssd1306 import SSD1306_I2C

i2c = I2C(0, sda=Pin(0),scl=Pin(1))

oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

screen1_row1 = "Pequeno mensaje:"
screen1_row2 = "Espero te guste lo siguiente"
screen1_row3 = "Es solo un"
screen1_row4 = "te amo pero"
screen1_row5 = "con mas pasos."


screen2_row1 = "Me gustas,porque"
screen2_row2 = "me complementas"
screen2_row3 = "me animas"
screen2_row4 = "Y sobre todo"
screen2_row5 = "nos apoyamos."

screen3_row1 = "Te amo"
screen3_row2 = "Mariana"
screen3_row3 = "Mi nina bella"
screen3_row4 = "<3"

screen1 = [[0, 0 , screen1_row1], [0, 15, screen1_row2], [0, 25, screen1_row3], [0, 35, screen1_row4], [0, 45, screen1_row5]]
screen2 = [[0, 0 , screen2_row1], [0, 15, screen2_row2], [0, 25, screen2_row3], [0, 35, screen2_row4], [0, 45, screen2_row5]]
screen3 = [[0, 0 , screen3_row1], [0, 15 , screen3_row2], [0, 25 , screen3_row3], [0, 35 , screen3_row4]]

def scroll_in_screen(screen):
  for i in range (0, oled_width+1, 4):
    for line in screen:
      oled.text(line[2], -oled_width+i, line[1])
    oled.show()
    if i!= oled_width:
      oled.fill(0)

def scroll_out_screen(speed):
  for i in range ((oled_width+1)/speed):
    for j in range (oled_height):
      oled.pixel(i, j, 0)
    oled.scroll(speed,0)
    oled.show()
    

while True:
    scroll_in_screen(screen1)
    sleep(4)
    scroll_out_screen(4)

    scroll_in_screen(screen2)
    sleep(3)
    scroll_out_screen(4)
    
    scroll_in_screen(screen3)
    sleep(2)
    scroll_out_screen(4)
