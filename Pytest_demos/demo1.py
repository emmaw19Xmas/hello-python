# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/25/2021 10:56 AM
# @Function:

import pytest

def inc(x):
    return x+1

def test_answer():
    assert inc(3) == 5
