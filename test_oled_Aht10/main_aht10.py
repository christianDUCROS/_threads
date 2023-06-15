#AHT10

from machine import Pin, SoftI2C
from time import sleep
import aht10  

#i2c = SoftI2C(scl=Pin(9), sda=Pin(8)) 
i2c = SoftI2C(scl=Pin(11), sda=Pin(10))
#init aht10
capteur_aht10 = aht10.AHT10(i2c) #adresse IC2 imposée

temperature = 0
humidite = 0
while True :
    capteur_aht10.command_mesure()
    humidite,temperature = capteur_aht10.lecture_mesure()
    humidite = round(humidite)
    temperature = round(temperature)
    print("Humidite (précision 2%)  : " , humidite, "Temperature (précision 0.3°C) :",temperature)

    sleep(0.5)