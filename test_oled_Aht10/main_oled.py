# test oled
from machine import Pin, SoftI2C
from time import sleep
import ssd1306


i2c = SoftI2C(scl=Pin(9), sda=Pin(8)) 

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

temperature = 0
humidite = 0
while True :
    oled.fill(0)
    oled.text('Capteur AHT10 ', 5, 0) 
    oled.text('Temperature : ', 0, 20) 
    oled.text(str(temperature), 100, 20) 
    oled.text('Humidite : ', 0, 40)
    oled.text(str(humidite),  100, 40)        
    oled.show()


