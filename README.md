# Parallel-Processing
*   Parallel computing is a type of computation in which many calculations or the execution of processes are carried out simuntaneously. Large problems can be often be divided into smaller ones, which can then be solved at the same time.

This can be done in two ways:

## Multiprocessing
* What ?
*    Multiprocessing refers to the ability of a system to support mote than one processore at the same time. Applications in a multiprocessing system are broken to smaller routines that run independently. The operating system allocates there threads to the processors improving performance of the system.

* Why ?
*    Consider a computer system with a single processor. It is assigned serveral processes at the same time, it will have to interrupt each task and switch briefly to another, to keep all the processes going.
The more tasks you must do at once, the more difficult it gets to keep track of them all, and keeping the timing right becomes more of a challenge.

### How ..
* A multiprocessing system can have:  
    1. multiprocessor, i.e. a comptuer with more than one central processor.
    2. multi-core processor, i.e. a single computing component with two or more independent actual processing units (called "cores").
    
     
### SHARING DATA BETWEEN PROCESSES
   In multiprocessing, any newly created process will do following:
   or we can say a child process will have the following properties
   * run independently
   * have their own memory space
 In 02_MP.py we have seen the parent list do not have values and is empty so here we will see the solution so how we can reflect the changes in the parent variable too.

#### SOLUTION 1
  * Method 1: SHARED MEMORY
    * multiprocessing module provides Array and Value objects to share data between processes.
        * Array: a ctype array allocated from shared memory
        * Value: a ctype object allocated from shared memory
    
    * ctype means like C/C++
    * In computers we have a portion called shared memory that can be accesed by multiprocessing so in shared memory we create a new array or value and these array and value are not your Basic python data structures the are something different and defined in multiprocessdin itself
#### SOLUTION 2
  * Method 2: SERVER PROCESS
    * Whenever a python starts, a server process is also started. From there on, whenever a new process is needed, the parent       process connnects to the server and requests it to fork a new process. A server process can hold Python objects and           allows other processes to manipulate them using proxies.
    * multiprocessing module provides a Manager class which controls a server process. Hence, managres provide a way tocreate       data which can be shared between different processes. 
    * Conclusion: if we normally execute the fucntion the append of fucntion insert will not reflect in fucntion print.
    For this we used this method. Here we have creater a manager object and then we defined a record which is saved in 
    server process beacuase we have manager.list this will save this list in my server process because manager is responsibel     for controlling server process. 
  `Server process ia a special type of process which gets initialize whenever Python program starts and it is                   responsible for communicating with all the parent process and the other child processes.`
 
 
### Communication between processes
    Effective use of multiple processes usually requires some communication between thhem, so that work
    can be divided and results can be aggregated.
#### Multiprocessing supports two types of communication channel between processes:
    * Queue. two end one for wrrite one for read
    * Pipe. two end both can be used for writing or reading both
* In the case of communication we have got a  channel. There is a communication channel whaich has two ends 
  so one end is used for writing the messages into it and from the other end you can read those messages.

#### METHOD 1 Queue:
    A simple way to commuunicate between process with multiprocessing is to use a Queue
    to pass messages back and forth. Any Python object can pass through a Queue.
     
#### METHOD 2 Pipes:
    A Pipe() can only have two endpoints.
    A Queue() can have multiple producers and consumers.
    If you need more than two points to communicate, use a Queue().
    If you need absolute performance, a Pipe() is much faster because Queue() is built on top of Pipe()

### Pooling between the process.

### Synchronization between processes
    Process synchronization is defined as a mechanism which ensures that two or more concurrent processes 
    do not simuntaneously execute some particular program segment known as critical section.
    Critical section refers to the parts of the program where the shared resource is accessed.
