# -*- coding: utf-8 -*-
# @Author  : Emma
# @Time    : 11/14/2021 10:25 AM
# @Function: import common modules.

import sys
import os
#
# print(dir())
# print("===============")
# print(dir(sys))
# print("===============")
# print(sys.path)
# print("===============")


# help(os)
# print(dir(os))
# print(os.name) #获取系统名称 nt -> windows, posix -> linux
# print(os.environ) #获取系统环境变量信息
# print(os.getenv('PATH')) #获取指定名称的环境变量信息
#执行系统指令
#os.system('pwd') #linux
#print(os.system('dir')) #windows

# print(os.getcwd())

print(sys.version)
print("===============")
print(sys.platform)
print("===============")
print(sys.argv)
print("===============")
#返回已导入的模块信息
print(sys.modules)
print("===============")
print(sys.modules.keys())
print("===============")
# 返回导包的搜索路径列表
print(sys.path)

"""sys模块常用方法"""
# 获取系统当前编码
print(sys.getdefaultencoding())
# print("===============")
# 运行时退出
sys.exit()
import time
