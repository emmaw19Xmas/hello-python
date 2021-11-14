# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/14/2021 3:52 PM
# @Function:
import json

data = [{'a':1,'b':2,'c':True, 'd':False, 'e':None}]

#将python对象编码为JSON字符串
json_data = json.dumps(data,indent=4)
print(json_data + "this is a json file")
print("============================")

#将JSON字符串钻吗为python对象
python_data = json.loads(json_data)
print(f"{python_data} this is a python object")
print("============================")

#写入json数据，再代码当前目录生成一个data.json文件
with open('data.json','w') as f:
    json.dump(data,f)
print("============================")

#读取数据，读取json文件并解码成python对象
with open('data.json', 'r') as f:
    data2 = json.load(f)
print(data2)
print(f"{python_data} this is a python object")