# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/29/2021 9:14 PM
# @Function:
# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/29/2021 9:06 PM
# @Function:pytest 作用域
import pytest

#所有测试用例进行之前，进行login操作一次
@pytest.fixture(scope='module')
def login():
    print("完成登录操作")

def test_search(login):
    print("搜索")

def test_cart(login):
    print("购物车")

def test_order(login):
    print("下单")