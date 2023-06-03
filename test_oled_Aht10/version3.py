#test oled et ATH10 en  mode thread
# Programmation asynchrone
from machine import Pin, SoftI2C
import ssd1306
from time import sleep
from aht10  import AHT10
from math import *

import _thread
lock = _thread.allocate_lock()

def core1_thread_AHT10() : #capteur
    global temperature
    global humidite
    i2c1 = SoftI2C(scl=Pin(11), sda=Pin(10))
    #init aht10
    capteur_aht10 = AHT10(i2c1) #adresse IC2 imposée
    while True:
        capteur_aht10.command_mesure()
        H,T = capteur_aht10.lecture_mesure()
        #lock.acquire() #non necessaire
        humidite = ceil(H)
        temperature = ceil(T)
        #lock.release() #non necessaire 
        print("Humidite (précision 2%)  : " , humidite, "Temperature (précision 0.3°C) :", temperature)
        sleep(0.5)
        
def core0_thread_oled() : #main
    global temperature
    global humidite
    i2c0 = SoftI2C(scl=Pin(9), sda=Pin(8)) 
    #init oled
    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c0)
    while True :
        oled.fill(0)
        oled.text('Temperature : ', 0, 0) 
        oled.text(str(temperature), 110, 0) 
        oled.text('Humidite : ', 0, 20)
        oled.text(str(humidite),  110, 20)        
        oled.show()
    
    

temperature = 0
humidite = 0

_thread.start_new_thread(core1_thread_AHT10, ()) #capteur
core0_thread_oled()  #main
    
