# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/20/2021 5:19 PM
# @Function:
'''
fesf
'''


import datetime

def timer(func):
    # 如果被装饰函数有参数，那么需要内函数加形参。
    # 但往往无法确定被装饰的参数的参数数量，所以把两个地方的参数全部换成不定长的参数
    def inner(*args, **kwargs):
        starttime = datetime.datetime.now()
        func(*args, **kwargs)
        endtime = datetime.datetime.now()
        print(f"execute time{endtime-starttime}")
    return inner

@timer # 添加装饰器之后，每当该函数被调用，timer就会启动
def hogwarts():
    print("hogwarts")

@timer
def add(a,b):
    print(a+b)


hogwarts()

add(10348235,234082)
