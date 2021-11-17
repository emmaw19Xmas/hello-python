# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/16/2021 9:59 PM
# @Function:
import time
import threading

def task2():
    time.sleep(5)
    print(2)

def task():
    time.sleep(5)
    print(1)

def main():
    start_time = time.time()
    # print(start_time)
    thread1 = threading.Thread(target = task)
    thread2 = threading.Thread(target = task2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    # a=3
    # print(f"线程2运行完了，a是{a}")
    end_time = time.time()# 会在这个线程开始的那一刻就运行
    # print(end_time)
    print(end_time-start_time)

if __name__=='__main__':
    main()


