# SHARING DATA BETWEEN PROCESSES
# In multiprocessing, any newly created process will do following:
# or we can say a child process will have the following properties
    # run independently
    # have their own memory space

import multiprocessing

result = []

def square_list(mylist):
    global result

    for num in mylist:
        result.append(num * num)
    print("Result: {}".format(result))

mylist = [1, 2, 3, 4, 5]

p1 = multiprocessing.Process(target=square_list, args=(mylist,))
p1.start()
p1.join()

print(result)  # It will be empty so here the parent class is empty while the child
# that is the result used in func is having some values, so this simply means both different
# processes have different memory spaces.