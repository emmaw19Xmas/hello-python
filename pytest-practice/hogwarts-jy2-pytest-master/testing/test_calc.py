"""
__author__ = 'hogwarts_xixi'
"""

# 测试类
# 命名规则：文件以test_开头，类以Test开头，方法以test_开头
import pytest
from pythonsource.calculator import Calculator


class TestCalc:
    def setup(self):
        # 每条用例执行之前需要执行setup
        print("开始计算")

    def teardown(self):
        # 每条用例执行之后需要执行teardown -- 方法级别
        print("结束计算")

    def teardown_class(self):
        # 这个类的所有用例执行之后执行teardown_class --- 类级别
        # 类级别：整个类只执行一次
        print("结束测试")

    @pytest.mark.add
    # @pytest.mark.parametrize(参数名, 参数值的列表或者元组)
    # 参数化的意思，将变化的测试数据，以参数的形式传递到测试用例当中，
    # 每一条测试数据，就是一条测试用例，在执行这条测试数据之前/后，也会执行setup/teardown
    @pytest.mark.parametrize("a,b,expect", [[1, 1, 2], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]])
    def test_add(self, a, b, expect):
        """"
        1. 第一个数输入 a ：1
        2. 第二个数输入 b ：1
        3. 预期结果为 expect：2
        """
        # 定义一个对象calc
        calc = Calculator()
        # result 为实际结果
        result = calc.add(a, b)
        # result 要与预期结果对比
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", [["文", 0.3, "TypeError"]])
    def test_add_error(self, a, b, expect):
        """
        1. 第一个数输入：文
        2. 第二个数输入：9.3
        3. 预期结果：TypeError
        :return:
        """
        # 定义一个对象calc
        calc = Calculator()
        # result 为实际结果
        with pytest.raises(eval(expect)) as e:
            result = calc.add(a, b)
        assert e.typename == expect

    @pytest.mark.div
    def test_div(self):
        pass
