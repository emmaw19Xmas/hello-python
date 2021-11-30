# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/29/2021 9:53 PM
# @Function:

#所有测试用例进行之前，进行login操作一次
import pytest


@pytest.fixture(scope='module')
def login():
    print("完成登录操作")
    user_name = 'emma'
    password = 'emma2019'
    yield user_name, password # 此处的yield更像是一个return功能
    print("退出登录")

@pytest.fixture(scope='module')
def connectDF():
    print("连接数据库")
    yield
    print("断开")
