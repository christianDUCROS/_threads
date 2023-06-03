from machine import Pin,SoftI2C
from time import sleep
from aht10  import AHT10
from math import *

i2c = SoftI2C(scl=Pin(9), sda=Pin(8))
capteur_aht10 = AHT10(i2c) #adresse IC2 imposée

#initilisation

#boucle principale
while True: 
    capteur_aht10.command_mesure()
    H,T = capteur_aht10.lecture_mesure()
    print("Humidite (précision 2%)  : " , ceil(H), "Temperature (précision 0.3°C) :", "{:.1f}".format(T))
    #print(ceil(H),end="; " )#arrpndi entier floor ou ceil
    #print("{:.1f}".format(T))# arrondi à 1 chiffre
    sleep(0.5)
