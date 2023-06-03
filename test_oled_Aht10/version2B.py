#test oled et ATH10 hors mode thread
#2 bus I2C

from machine import Pin, SoftI2C
import ssd1306
from time import sleep
from aht10  import AHT10
from math import *


i2c0 = SoftI2C(scl=Pin(9), sda=Pin(8)) 
i2c1 = SoftI2C(scl=Pin(11), sda=Pin(10))
#init oled
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c0)
#init aht10
capteur_aht10 = AHT10(i2c1) #adresse IC2 imposée

temperature = 0
humidite = 0
while True :
    capteur_aht10.command_mesure()
    H,T = capteur_aht10.lecture_mesure()
    humidite = ceil(H)
    temperature = ceil(T)
    print("Humidite (précision 2%)  : " , humidite, "Temperature (précision 0.3°C) :", temperature)
    #print(ceil(H),end="; " )#arrpndi entier floor ou ceil
    #print("{:.1f}".format(T))# arrondi à 1 chiffre
    
    oled.fill(0)
    oled.text('Temperature : ', 0, 0) 
    oled.text(str(temperature), 110, 0) 
    oled.text('Humidite : ', 0, 20)
    oled.text(str(humidite),  110, 20)        
    oled.show()

    sleep(0.5)