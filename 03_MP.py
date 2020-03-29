'''
Communication between processes
    Effective use of multiple processes usually requires some communication between thhem, so that work
    can be divided and results can be aggregated.
Multiprocessing supports two types of communication channel between processes:
    1. Queue. two end one for wrrite one for read
    2. Pipe. two end both can be used for writing or reading both

In the case of communication we have got a  channel. There is a communication channel whaich has two ends 
so one end is used for writing the messages into it and from the other end you can read those messages.
'''

# METHOD 1 Queue:
    # A simple way to commuunicate between process with multiprocessing is to use a Queue
    # to pass messages back and forth. Any Python object can pass through a Queue.

import multiprocessing

def square_list(myList, q):
    for num in myList:
        q.put(num*num)

def print_list(q):
    while not q.empty():
        print(q.get())

q = multiprocessing.Queue()

p1 = multiprocessing.Process(target=square_list, args=([1,2,3,4,5], q))
p2 = multiprocessing.Process(target=print_list, args=(q,))

p1.start()
p2.start()

p1.join()
p2.join()