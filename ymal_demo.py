# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/20/2021 10:49 AM
# @Function:

import yaml
data = {
    "client": {"default-charactor-set":"utf-8"},
    "mysql": {"user": 'root', "password": 123},
    "custom": {
        "user1": {"user":"Emma","pwd": 666},
        "user2": {"user":"Shane","pwd":999},
    }
}
#用dump方法把python对象转为yaml 文档
with open('./my.yaml', 'w', encoding="utf-8") as f:
    yaml.dump(data,f)


#读取yaml文件
file_path = './my.yaml'
with open(file_path, 'r', encoding='utf=8')as f2:
    data2 = yaml.safe_load(f2)
print(data2)

#取user的姓名
user1_name = data2['custom']['user1']['user']
print(user1_name)