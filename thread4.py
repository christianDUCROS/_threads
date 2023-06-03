import _thread
lock = _thread.allocate_lock()

def core1_thread():
    print("J’utilise le coeur 1")
    lock. release()


#main
print('debut boucle du core0')
while True :
    print("J’utilise le coeur 0")
    lock.acquire()
    _thread.start_new_thread(core1_thread, ())
    lock.acquire()
    lock.release()
    print('je termine mon main')

