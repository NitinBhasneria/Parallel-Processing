# In python , the multiprocessing module includes a very simple and intuitive API
# for dividing work between multiple processes.
import os # Gives access to some operating system module

def print_cube(num):
    print(os.getpid()) # gives id or actual process running at the instance
    print("Cube: {}".format(num*num*num))

def print_square(num):
    print(os.getpid())
    print("Sqaure: {}".format(num*num))

# We have to call it as 
# print_cube(3)
# print_square(3)

# But we want a situation in which we can call both simuntaneously

import multiprocessing

print(multiprocessing.cpu_count())  #how many cores in your cpu you have

# We have 8 cores (multiprocessing units)
# If we give more than 8 processes, then it will not be an 
#   ideal multiprocessing.


# Now we are making a process by following command
p1 = multiprocessing.Process(target = print_cube, args = (3,))
p2 = multiprocessing.Process(target = print_square, args = (3,))
# Process is a class in multiprocessing module which takes a task to be executed.
# We pass the task by target and arguments by args. In the args you have to provide 
#   a tuple in which you pass your non keywords arguments.


# Now we have a process p1 and p2 and these processes have multiple methods.
# For startin the process

# p1.start()  

# # This actually sends a comand to the cpu to start the process 
# and this process starts but if you write any command just below it let us 
# say print("Hello") so it will print the Hello no matter the process p1 is 
# completed or not and so for waiting for p1 to complete we write

#p1.join() 

# make program wait until p1 is completed. 

# Now we start p2 after p1.join() then it does not make sense as it will
# start after completing the p1 process but we want to start with p1 processing
#  so the code will be
print("Start")
p1.start()
p2.start()

p1.join()
p2.join()
print("DONE")

print(p1.is_alive())  # To check if process is still alive or not.
