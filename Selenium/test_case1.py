# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/5/2021 7:50 PM
# @Function:

"""
1. 导入库
"""
from selenium import webdriver

class test_Home():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize.Chrome()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()


    def test_target(self):
        pass