'''
Method 2: SERVER PROCESS
    Whenever a python starts, a server process is also started. From there on, 
    whenever a new process is needed, the parent process connnects to the server 
    and requests it to fork a new process. A server process can hold Python 
    objects and allows other processes to manipulate them using proxies.

    multiprocessing module provides a Manager class which controls a server process.
    Hence, managres provide a way tocreate data which can be shared between 
    different processes. 
'''

import multiprocessing

def print_record(records):
    for record in records:
        print("Name: {0}\nScore: {1}\n".format(record[0], record[1]))

def insert_record(record, records):
    records.append(records)
    print("New record added!\n")


with  multiprocessing.Manager() as manager:  # created a manager object
    records = manager.list([('Sam', 10), ('Adam', 9), ('Kevin',9)]) 
    new_record = ('jeff', 8)

    p1 = multiprocessing.Process(target=insert_record, args=(new_record, records))
    p2 = multiprocessing.Process(target=print_record, args=(records,))

    p1.start()
    p1.join()

    p2.start()
    p2.join()
 
'''puting list in manager i.e. in server process server process contains all thode 
Python data structure taht you want to share between different processes and how to
do that it is done by this manager as above.'''


''' Conclusion: if we normally execute the fucntion the append of fucntion insert will 
not reflect in fucntion print.
For this we used this method
Here we have creater a manager object. and then we defined a record which is saved in 
server process beacuase we have manager.list this will save this list in my server
process because manager is responsibel for controlling server process. 
Server process ia a special type of process which gets initialize whenever Python program
starts and it is responsible for communicating with all the parent process and the 
other child processes.
'''