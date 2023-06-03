import utime
import _thread

def core1_thread():
    i = 0
    while True :
        print("J’utilise le coeur 1")
        i += 1
        utime.sleep(2)
        if i == 5 : 
            raise SystemExit

_thread.start_new_thread(core1_thread, ())

# main
while True :
    print('debut boucle du core0',utime.ticks_ms())
    print("J’utilise le coeur 0")
    utime.sleep(5)