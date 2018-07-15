# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018/7/14 20:48'
import multiprocessing as mp
import threading as td
import time

def job(q):
    res = 0
    for i in range(1000000):
        res+= i+i**2+i**3
    q.put(res)
def normal():
    res =0
    for _ in range(2):
        for i in range(1000):
            res += i +i**2 +i**3


def multiprocessing():
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multiprocessing',res1,res2)
def multithreading():
    q = mp.Queue()
    p1 = td.Thread(target=job, args=(q,))
    p2 = td.Thread(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread',res1, res2)
if __name__=='__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time ',st1-st)
    multithreading()
    st2 = time.time()
    print('multithread',st2-st1)
    multiprocessing()
    st3 = time.time()
    print('multiprocessing',st3-st2)