#test oled et ATH10 en mode thread


# test oled
from machine import Pin, SoftI2C
import ssd1306
from time import sleep



i2c = SoftI2C(scl=Pin(9), sda=Pin(8)) 

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

temperature = 30
humidite = 40
while True :
    oled.fill(0)
    oled.text('Temperature : ', 0, 0) 
    oled.text(str(temperature), 100, 0) 
    oled.text('Humidite : ', 0, 20)
    oled.text(str(humidite),  100, 20)        
    oled.show()


