# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/7/2021 9:30 PM
# @Function:
from time import sleep

from selenium import webdriver

class TestActionChain():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    def test_register(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        sleep(3)
        w1 = self.driver.current_window_handle
        print(w1)
        self.driver.find_element_by_link_text("立即注册").click()
        sleep(3)
        w2 = self.driver.current_window_handle
        print(w2)
        #print(self.driver.window_handles)
        self.driver.switch_to.window(w2)

        self.driver.find_element_by_name("userName").send_keys("emmaw4725")
        sleep(3)