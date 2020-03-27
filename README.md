# Parallel-Processing
*   Parallel computing is a type of computation in which many calculations or the execution of processes are carried out simuntaneously. Large problems can be often be divided into smaller ones, which can then be solved at the same time.

This can be done in two ways:

# Multiprocessing
* What ?
*    Multiprocessing refers to the ability of a system to support mote than one processore at the same time. Applications in a multiprocessing system are broken to smaller routines that run independently. The operating system allocates there threads to the processors improving performance of the system.

* Why ?
*    Consider a computer system with a single processor. It is assigned serveral processes at the same time, it will have to interrupt each task and switch briefly to another, to keep all the processes going.
The more tasks you must do at once, the more difficult it gets to keep track of them all, and keeping the timing right becomes more of a challenge.

* How ..
* A multiprocessing system can have:  
    1. multiprocessor, i.e. a comptuer with more than one central processor.
    2. multi-core processor, i.e. a single computing component with two or more independent actual processing units (called "cores").
    