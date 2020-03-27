''' In 02_MP.py we have seen the parent list do not have values and is empty so here 
we will see the solution so how we can reflect the changes in the parent variable too.

SOLUTION 1

Method 1: Shared memory
    multiprocessing module provides Array and Value objects to share data between processes.

    Array: a ctype array allocated from shared memory
    Value: a ctype object allocated from shared memory
  ctype means like C/C++
In computers we have a portion called shared memory that can be accesed by multiprocessing
so in shared memory we create a new array or value and these array and value are not your 
basic python data structures the are something different and defined in multiprocessdin itself
'''
import multiprocessing

def square_list(mylist, result, square_sum):

    for idx, num in enumerate(mylist):
        result[idx] = num*num      # we have to access of ctype array by index method like result[0]

    square_sum.value = sum(result) # For accessing the values of value object you have to do .value

mylist = [1,2,3,4]

result = multiprocessing.Array('i', 4)  # i for int and 4 is a size
square_sum = multiprocessing.Value('i') # i for int

p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum))

p1.start()
p1.join()

for i in range(4):
    print(result[i])

# here we have the change reflected back in parent process