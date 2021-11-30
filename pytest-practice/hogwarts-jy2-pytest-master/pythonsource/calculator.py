"""
__author__ = 'hogwarts_xixi'
"""


class Calculator:
    def add(self, a, b):
        """
        相加方法
        :param a:
        :param b:
        :return:
        """

        if a > 99 or a < -99 or b > 99 or b < -99:
            print("请输入范围为【-99, 99】的整数或浮点数")
            return "参数大小超出范围"

        return a + b

    def div(self, a, b):
        """
        相除方法
        :param a:
        :param b:
        :return:
        """
        if a > 99 or a < -99 or b > 99 or b < -99:
            print("请输入范围为【-99, 99】的整数或浮点数")
            return "参数大小超出范围"

        return a / b
