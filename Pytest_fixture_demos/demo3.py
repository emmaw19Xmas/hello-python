# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/29/2021 9:29 PM
# @Function: yield
import pytest

#所有测试用例进行之前，进行login操作一次
@pytest.fixture(scope='module')
def login():
    print("完成登录操作")
    user_name = 'emma'
    password = 'emma2019'
    yield user_name, password # 此处的yield更像是一个return功能
    print("退出登录")

def test_search(login):
    print("搜索")

def test_cart(login):
    u, p = login
    print("购物车")
    print(f"username is {u}")

def test_order(login):
    print("下单")