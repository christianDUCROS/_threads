# test _thread lock object 
import _thread

# create lock
lock = _thread.allocate_lock()
print(type(lock))

# Etat du lock 
print(lock.locked())

# acquire and release
lock.acquire()
lock.acquire()
print(lock.locked())
lock.release()
print(lock.locked())
