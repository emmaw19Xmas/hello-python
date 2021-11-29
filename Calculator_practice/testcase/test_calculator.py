# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 11/28/2021 3:11 PM
# @Function:

import pytest
from conda.common.serialize import yaml

from Calculator_practice.func.calculator import Calculator

class TestAdd:

    def setup_class(self):
        self.cal = Calculator()

    def teardown_class(self):
        print("结束计算")

    def setup(self):
        print("开始测试")

    def teardown(self):
        print("结束测试")


    @pytest.mark.parametrize('x1,x2,expected', [[1, 1, 2]])
    def test_add(self, x1, x2, expected):
        assert self.cal.add(x1, x2) == expected

    @pytest.mark.parametrize('x1,x2,expected', [[-0.01, 0.02, 0.01]])
    def test_add2(self, x1, x2, expected):
        assert self.cal.add(x1, x2) == expected

    @pytest.mark.parametrize('x1,x2,expected', [[10, 0.02, 10.02]])
    def test_add3(self, x1, x2, expected):
        assert self.cal.add(x1, x2) == expected

    @pytest.mark.parametrize('x1,x2,expected', [[98.99, 99, 197.99]])
    def test_add4(self, x1, x2, expected):
        assert self.cal.add(x1, x2) == expected

    @pytest.mark.parametrize('x1,x2,expected', [[99, 98.99, 197.99]])
    def test_add5(self, x1, x2, expected):
        assert self.cal.add(x1, x2) == expected

    @pytest.mark.parametrize('x1,x2,expected', [[-98.99, -99, -197.99]])
    def test_add6(self, x1, x2, expected):
        assert self.cal.add(x1, x2) == expected

    @pytest.mark.parametrize('x1,x2,expected', [[-99, -98.99, -197.99]])
    def test_add7(self, x1, x2, expected):
        assert self.cal.add(x1, x2) == expected



    @pytest.mark.parametrize('x1,x2,expected', [["文", 9.3, "TypeError"]])
    def test_add12(self, x1, x2, expected):
        with pytest.raises(eval(expected)) as e:
            result = self.cal.add(x1, x2)
        assert e.typename == expected



    # @pytest.mark.parametrize('x1,x2,expected', [[4, "字", "参数大小超出范围"]])
    # def test_add13(self, x1, x2, expected):
    #     assert self.cal.add(x1, x2) == "参数大小超出范围"