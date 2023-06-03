import utime 
import _thread
lock = _thread.allocate_lock() # create a global lock

def core1_thread():
    k = 0
    while True:
        while not lock.acquire(0): #fonction en attendant la libération du verrou
            k += 1
            
        #unlock par le core 0 and lock par le core 1   
        print('k = ',k)
        lock.release()


def core0_thread():
    while True:
        lock.acquire()
        print("J’utilise le coeur 0")
        utime.sleep(5)
        lock.release()

second_thread = _thread.start_new_thread(core1_thread, ())
core0_thread()
