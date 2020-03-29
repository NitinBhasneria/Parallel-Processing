'''
METHOD 2
A Pipe() can only have two endpoints.
A Queue() can have multiple producers and consumers.
If you need more than two points to communicate, use a Queue().
If you need absolute performance, a Pipe() is much faster because 
    Queue() is built on top of Pipe()
'''
import multiprocessing

msgs = ["Hey", "Hello", "Hru?", "END"]

def send_msgs(conn, msgs):
    for msg in msgs:
        conn.send(msg)
    conn.close()

def recv_msg(conn):
    while 1:
        msg = conn.recv()
        if msg == "END":
            break;
        print(msg)

parent_conn, child_conn = multiprocessing.Pipe()

p1 = multiprocessing.Process(target=(send_msgs), args=(parent_conn,msgs))
p2= multiprocessing.Process(target=recv_msg, args=(child_conn, ))

p1.start()
p2.start()

p1.join()
p2.join()

''' Data in a pipe becomes corrupted if two processes(or threads) try to read 
from or write to the same end of the pipe at the same time. Of course there is no risk of 
corruption from the processes using different ends of the pipr at the same time.
Also note that, Queue do proper syncronization between processes, at the expense of more complexity.
Hence, queues are said to be thread and process safe.'''