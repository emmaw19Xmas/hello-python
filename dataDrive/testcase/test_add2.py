# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/27/2021 9:25 AM
# @Function:
import pytest
from dataDrive.func.operation import my_add

# 读取 data目录下的 params.csv 文件
import csv

def get_csv():
    """
    获取csv数据
    :return: 返回数据的结构：[[1, 1, 2], [3, 6, 9], [100, 200, 300]]
    """
    with open('../data/param.csv', 'r') as file:
        raw = csv.reader(file)
        data = []
        for line in raw:
            data.append(line)
    print(data)
    return data

class TestWithCSV:
    #@pytest.mark.parametrize('x,y,expected', [[1, 1, 2]])
    @pytest.mark.parametrize('x,y,expected', get_csv())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)