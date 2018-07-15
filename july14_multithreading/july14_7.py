# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018\7\14 0014 13:14'
import multiprocessing as mp

def job(q):
    res=0
    for i in range(3):
        res+=i+i**2+i**3
    q.put(res)    #queue

if __name__=='__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1,res2)