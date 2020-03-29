# Pooling between the process
import multiprocessing

def square (n):
    return n*n

mylist = [1,2,3,4,4,5,6,3,6,5]
result = []

p = multiprocessing.Pool()

result = p.map(square, mylist)

print(result)