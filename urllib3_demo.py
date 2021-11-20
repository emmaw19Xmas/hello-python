# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/20/2021 3:54 PM
# @Function:
import json

import urllib3

def test_HTTP():
    # 创建线程池对象，默认会校验证书
    pm = urllib3.PoolManager()
    # 发送HTTP请求
    res = pm.request(method='GET', url="http://httpbin.org/robots.txt")

    print(type(res))
    print(res.status)  # 查看响应状态状态码
    print(res.headers)  # 查看响应头信息
    print(res.data)  # 查看响应原始二进制信息

def test_response():
    pm = urllib3.PoolManager()
    resp = pm.request(method='GET', url="http://httpbin.org/ip")

    # 获取二进制形式的响应内容
    raw = resp.data
    print(type(raw), raw)
    # 使用utf-8解码成字符串
    content = raw.decode('utf-8')
    print(type(content), content)
    # 将JSON字符串解析成字典对象
    dict_obj = json.loads(content)
    print(type(dict_obj), dict_obj)
    print(dict_obj['origin'])


def test_headers():
    pm = urllib3.PoolManager()
    url = "http://httpbin.org/get"

    # 定制请求头
    headers = {'School': 'hogwarts'}
    resp = pm.request('GET', url, headers=headers)
    # 查看相应信息
    content = json.loads(resp.data.decode('utf-8'))
    print(content['headers'])