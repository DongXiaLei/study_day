from datetime import datetime
import numpy
import sys

def numpysum(n):
    a = numpy.arange(n)**2
    b = numpy.arange(n)**3
    c = a+b
    return c
def pythonsum(n):
    a = list(range(n))
    b = list(range(n))
    c=[]

    for i in range(len(a)):
        a[i] = i**2
        b[i] = i**3
        c.append(a[i]+b[i])
    return c

size = int(sys.argv[1])
start = datetime.now()
c = pythonsum(size)
count = datetime.now()-start
print(count)

start = datetime.now()
c = numpysum(size)
count = datetime.now()-start
print(count)
