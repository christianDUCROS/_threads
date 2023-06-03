
#version1
import _thread
import utime

def core1_thread() : #capteur 	    
    while True:
        print("J’utilise le coeur 1")
        utime.sleep(2)
    
def core0_thread() : #main    
    while True :
        print('debut boucle du core0',utime.ticks_ms())
        print("J’utilise le coeur 0")
        utime.sleep(5)

_thread.start_new_thread(core1_thread, ()) #capteur
core0_thread()  #main

'''
#version2
import _thread
import utime

def core1_thread() :
    while True:
        print("J’utilise le coeur 1")
        utime.sleep(2)
    
#main core0_thread 
th1 = _thread.start_new_thread(core1_thread, ())
while True :
    print('debut boucle du core0',utime.ticks_ms())
    print("J’utilise le coeur 0")
    utime.sleep(5)
'''