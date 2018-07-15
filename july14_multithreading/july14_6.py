# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018\7\14 0014 13:08'
import multiprocessing as mp

def jod(a,b):
    print('a=%d,b=%d'%(a,b))

def main():
    p1 = mp.Process(target=jod,args=(1,2))
    p1.start()
    p1.join()

if __name__== '__main__':
    main()