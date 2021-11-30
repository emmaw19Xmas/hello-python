# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/29/2021 10:14 PM
# @Function:
import pytest


@pytest.fixture(params=[['selenium',123],['appium',456]])
def login(request):
    print(f"完成登录操作{request.param}")


def test_cart(login):
    print("购物车")
    print(f"username is {login}")