# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/29/2021 9:06 PM
# @Function: pytest介绍
import pytest


@pytest.fixture()
#定义了fxiture的方法，尽量不要用test开头。比如不要test_login()
def login():
    print("完成登录操作")

def test_search():
    print("搜索")

def test_cart(login):
    print("购物车")

def test_order():
    print("下单")