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

'''
#fonction time out dans le thread
import utime as time
import _thread

def core1_thread():
    start = time.ticks_ms()
    while True :
        print("J’utilise le coeur 1")
        time.sleep(2)
        delta = time.ticks_diff(time.ticks_ms(), start)
        if delta  > 10000 : 
            raise SystemExit

_thread.start_new_thread(core1_thread, ())

# main
while True :
    print('debut boucle du core0',time.ticks_ms())
    print("J’utilise le coeur 0")
    time.sleep(5)
'''
