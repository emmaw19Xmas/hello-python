# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/29/2021 9:53 PM
# @Function: pytest 之conftest。
import pytest
"""
- 系统执⾏到参数 login 时先从本模块中查找是否有这个名字的变量什么的，
- 之后在 conftest.py 中找是否有。
"""

def test_search(login,connectDF):
    print("搜索")

def test_cart(login):
    u, p = login
    print("购物车")
    print(f"username is {u}")

def test_order(login):
    print("下单")