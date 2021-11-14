# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/14/2021 10:54 AM
# @Function:
def div(a,b):
    return a/b

try:
    print(div(1,0))
except ZeroDivisionError as e:
    print("此处有除零异常")


try:
    print(div(1,0))
except Exception as e:
    print("此处有除零异常")

finally:
    print("如果有收尾的需要，可以把收尾的命令写在fianlly里。"
          "无论有无异常，finally里的语句都会执行")
print("===============")
def set_Age(num):
    if num<=0 or num>100:
        raise ValueError(f"值错误{num}")
    else:
        print(f"设置的年龄为{num}")
set_Age(80)
set_Age(120)
"""
Traceback (most recent call last):
  File "D:/Python_H/exception.py", line 29, in <module>
    set_Age(120)
  File "D:/Python_H/exception.py", line 25, in set_Age
    raise ValueError(f"值错误{num}")
ValueError: 值错误120
"""

"""自定义异常"""
class MyException(Exception):
    def __init__(self,msg):
        print(f"这是一个异常{msg}")

