# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/7/2021 10:05 PM
# @Function:
import os
from selenium import webdriver


class Base():
    def setup(self):
        # browser = os.getenv("browser")
        # if browser == 'firefox':
        #     self.driver = webdriver.Firefox()#前提：给firefox webdriver好环境变量
        # elif browser == "headless":
        #     self.driver = webdriver.PhantomJS()
        # else:
        #     self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()