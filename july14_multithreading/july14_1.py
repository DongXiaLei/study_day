# _*_ coding: utf-8 _*_
__author__ = 'Xialei'
__date__ = '2018\7\14 0014 9:25'
import threading
def thread_jod():
    print('this is a thread is %s'%threading.current_thread())
def main():
    add_thread = threading.Thread(target=thread_jod)
    add_thread.start()
    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())

if __name__=='__main__':
    main()