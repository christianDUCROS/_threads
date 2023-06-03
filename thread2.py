import _thread
import utime

def core1_thread() : #capteur 	    
    print("J’utilise le coeur 1")
    utime.sleep(10)
    
#main    
while True :
    print('debut boucle du core0',utime.ticks_ms())
    print("J’utilise le coeur 0")
    try:
        _thread.start_new_thread(core1_thread, ())
        break
    except OSError:
        pass
    utime.sleep(5)