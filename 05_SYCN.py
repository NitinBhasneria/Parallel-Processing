# Synchronization between processes

'''
Process synchronization is defined as a mechanism which ensures that two or more
concurrent processes do not simuntaneously execute some particular program 
segment known as critical section.

Critical section refers to the parts of the program where the shared resource is accessed.
'''

import multiprocessing

def decrease(b, lock):
    for  _ in range(1000):
        lock.acquire()
        b.value = b.value - 1
        lock.release()

def increase(b, lock):
    for _ in range(1000):
        lock.acquire()
        b.value = b.value + 1
        lock.release()

def perfor():
    b = multiprocessing.Value('i', 100)

    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=decrease, args=(b, lock))
    p2 = multiprocessing.Process(target=increase, args=(b, lock))
    
    p1.start()
    p2.start()    

    p1.join()
    p2.join()
    
    print("Final balance: {}".format(b.value))

for _ in range(10):
    perfor()


