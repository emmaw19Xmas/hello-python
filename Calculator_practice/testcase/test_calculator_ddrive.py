# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/28/2021 4:57 PM
# @Function:

import pytest
from conda.common.serialize import yaml

from Calculator_practice.func.calculator import Calculator

def get_yaml(level):
    """
        获取yaml数据
        :return: 返回数据的结构：[[1, 1, 2], [3, 6, 9], [100, 200, 300]]
        """
    with open('../data/test_data.yml', 'r',encoding='utf=8') as file:
        yaml_d = yaml.safe_load(file)
        #只读取p0和p1的data
        p = yaml_d['add'][level]['datas']
        return p


class TestAdd:

    def setup_class(self):
        self.cal = Calculator()

    def teardown_class(self):
        print("结束计算")

    def setup(self):
        print("开始测试")

    def teardown(self):
        print("结束测试")

    @pytest.mark.parametrize('x1,x2,expected', get_yaml('P0'))
    def test_add(self, x1, x2, expected):
        assert self.cal.add(x1, x2) == expected
    @pytest.mark.parametrize('x1, x2, expected', get_yaml('P2'))
    def test_add_error(self, x1, x2, expected):
        with pytest.raises(eval(expected)) as e:
            self.cal.add(x1, x2)
        assert e.typename == expected