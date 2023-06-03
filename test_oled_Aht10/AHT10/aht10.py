"""
MicroPython AHT10 Digital Humidity Temperature Sensor
"""
from utime import sleep_ms

# registers
_AHT10_SOFT_RESET_CMD  = const(0xBA) # soft reset commande
_AHT10_INIT_CMD  = const(0xE1) # initialization command 
_AHT10_TRIGGER_MEASUREMENT_CMD = const(0xAC) # Trigger measurement
_AHT10_DATA0 = const(0x33) # Data trigger measurement
_AHT10_DATA1 = const(0x00) # Data trigger measurement

_AHT10_SOFT_RESET_DELAY = const(20) #20ms apres un reset
_AHT10_CMD_DELAY=const(350)
_AHT10_MEASUREMENT_DELAY = const(80)

class AHT10:
    def __init__(self, bus): 
        self._i2c = bus
        self._address = 0x38 #adresse prédéfinie
        self._buf2 = bytearray(2)
        self._buf3 = bytearray(3)
        self._DataBuffer = bytearray(6)#mesures des datas
        
        self.soft_reset() 
        self.init_command() #initilisation des commandes

    
    def soft_reset(self):
        self._i2c.writeto(self._address, bytes(_AHT10_SOFT_RESET_CMD))
        sleep_ms(_AHT10_SOFT_RESET_DELAY)
        
    def init_command(self):
        self._buf2[0] = _AHT10_INIT_CMD 
        self._buf2[1] = _AHT10_TRIGGER_MEASUREMENT_CMD
        self._i2c.writeto(self._address, self._buf2)
        sleep_ms(_AHT10_CMD_DELAY)
        
    def command_mesure(self):
        self._buf3[0]=_AHT10_TRIGGER_MEASUREMENT_CMD
        self._buf3[1]=_AHT10_DATA0
        self._buf3[2]=_AHT10_DATA1
        self._i2c.writeto(self._address, self._buf3)
        sleep_ms(_AHT10_MEASUREMENT_DELAY)
    
    
    def lecture_mesure(self):
        #acquisition de l'humidité et de la température
        try :     
            self._DataBuffer =self._i2c.readfrom(self._address, 6)
        except :
            return ('erreur I2C')
        #calcul de l'humidité
        Raw_humidite = ((self._DataBuffer[1] << 16) | (self._DataBuffer[2] << 8) | (self._DataBuffer[3]))>>4
        humidite = Raw_humidite * 0.000095; # humidité en %
        if humidite < 1:
            humidite= 0
        if humidite> 99:
            humidite=100
        #calcul de la température
        Raw_temperature = ((self._DataBuffer[3] & 0x0F) << 16) | (self._DataBuffer[4] << 8) | self._DataBuffer[5]
        temperature = Raw_temperature * 0.000191 - 50;  # temperature data °C
        #return (humidite, temperature)
        return humidite, temperature
    
    
   
    
    
    