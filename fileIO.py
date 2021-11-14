# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/14/2021 2:05 PM
# @Function: how to read and write files via Python

file = open('demo.txt','r',encoding='UTF-8')

print(file.read(100)) #只读取前100个字符；换行符也是一个字符

print("---------------")
print(file.readlines(2))#


print(file.read(100)) #只读取前100个字符；换行符也是一个字符
file.seek(0) #把光标设置回开头处
print("---------------")
print(file.readlines())#

file.close()

with open('demo.txt', 'w', encoding ='utf-8') as f:
		print(f.write("emma is studying python 2021"))
        #print(file.read())
print(f.closed)


