# Thread synchronization
# Prevents the threads to be processed at same time
''' Global variables are going to be a part of critical section so if you have a thread 
adn that is executing any function and in that section if there is any line which is 
reffering to a critical section (Global variable here) and if multiple threads are 
trying to execute the crtical section at the same time, it will give some unexpected output.
'''

import threading
x = 0


def increase():
    global x
    x += 1

def task(lock):
    for _ in range (100000):
        lock.acquire()
        increase()
        lock.release()

def main():
    global x
    x = 0

    lock = threading.Lock()

    t1 = threading.Thread(target=task, args=(lock, ))
    t2 = threading.Thread(target=task, args=(lock, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

for i in range(10):
    main()
    print("Iteration {0}: x = {1}".format(i,x))
