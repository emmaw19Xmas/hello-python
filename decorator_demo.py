# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/20/2021 5:19 PM
# @Function:
def timer(func):
    def inner():
        print("timer start")
        func()
        print("timer end")
    return inner

@timer # 添加装饰器之后，每当该函数被调用，timer就会启动
def hogwarts():
    print("hogwarts")


hogwarts()