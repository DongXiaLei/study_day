# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018\7\14 0014 10:19'

import threading
from time import ctime,sleep

def music(func):
    for i in range(2):
        print('I am listening music %s--%s'%(func,ctime()))
        sleep(1)
def movie(func):
    for i in range(2):
        print('I am watching movie %s--%s'%(func,ctime()))
        sleep(5)

threads =[]

t1= threading.Thread(target=music,args=('aiqing',))
threads.append(t1)
t2 = threading.Thread(target=movie,args=('afadan',))
threads.append(t2)

def main():
    for i in threads:
        i.setDaemon(True)
        i.start()

    i.join()
    print("all over %s" %ctime())
if __name__=='__main__':
    main()