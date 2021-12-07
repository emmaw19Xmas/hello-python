# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/6/2021 9:31 PM
# @Function:
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.keys import Keys


class TestTouchChain():
    def setup(self):

        self.driver = webdriver.Chrome(options={'w3c':False})
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    def test_touchactionscroll(self):
        self.driver.get("https://www.baidu.com")
        el = self.driver.find_element_by_id("kw")
        el_search = self.driver.find_element_by_id("su")
        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(el_search)

        action.perform()
        sleep(5)
        action.scroll_from_element(el,0,10000).perform()
        sleep(3)