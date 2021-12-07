# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/5/2021 8:21 PM
# @Function:
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.get("https://ceshiren.com/")
        self.driver.implicitly_wait(3)

    def test_wait(self):
        self.driver.find_element_by_id("ember362").click()
        # def wait(x):
        #     return len(self.driver.find_element_by_link_text("/t/topic/13228"))>=1
        """有时也可以不写wait方法，换用expected_condition"""
        expected_conditions.visibility_of_element_located()

        WebDriverWait(self.driver, 10).until(wait)
        self.driver.find_element_by_link_text("/t/topic/13228").click()


