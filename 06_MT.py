## Multithreading


'''
A thread is an entity within a process that can be scheduled for execution. 
Also, it is athe smallest unit of processing that cab be performed in an OS(Operating system).
In simple words, a thread is a sequence of such instruction within a program that can be executed
independently of other code. For simplicity, youcan assume that a thread is simply a subset of a process.


### Multiple threads can exist within one process where:
    * Each thread contains its own register set and local variables(stored in stack).
    * All the threads of a process share global variables (stored in heap) and the program code.
'''

### Multithreading is defined as a abitlity of a processor to execute multiple threads concurrently.

import threading
import os
import multiprocessing

def print_cube(num):
    print(threading.current_thread().name, os.getpid())
    print("Cube :{}".format(num * num * num))

def print_square(num):
    print(threading.current_thread().name, os.getpid())
    print("Square :{}".format(num * num))

t1 = threading.Thread(target=print_cube, args=(3,), name = 't1')
t2 = threading.Thread(target=print_square, args=(3,), name = 't2')

t1.start()
t2.start()

t1.join()
t2.join()

# You will get the same process. Here the context switching is happening.