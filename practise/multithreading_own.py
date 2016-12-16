#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import time
import threading


# Assume this is the saving amount
balance = 0
lock = threading.Lock()


def chaneg_it(n):
    global balance
    balance += n
    balance -= n


def run_thread(n):
    for i in range(100000):
        # Acquire the lock
        lock.acquire()
        try:
            chaneg_it(n)
        finally:
            # Release the lock after change
            lock.release()


# The code for creating new thread
def loop():
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s ended." % threading.current_thread().name)


def main():
    # Test 2
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print balance

    # Test 1
    # print("thread %s is running..." % threading.current_thread().name)
    # t = threading.Thread(target=loop, name='LoopThread')
    # t.start()
    # t.join()
    # print("thread %s ended." % threading.current_thread().name)


if __name__ == '__main__':
    main()
