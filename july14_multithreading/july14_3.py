# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018\7\14 0014 10:52'

import threading
from time import sleep

from queue import Queue

def job(l,q):
    for i in range(len(l)):
        l[i] = l[i]**2
        # sleep(1)
    q.put(l)

def multithreading():
    q =Queue()
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    for i in range(4):
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)

if __name__=='__main__':
    multithreading()