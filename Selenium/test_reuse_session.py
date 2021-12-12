# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/11/2021 4:36 PM
# @Function:
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Selenium.base import Base


class TestReuse(Base):
    def test_reuse_session(self):
        option = Options()
        option.debugger_address = 'localhost:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://ezrouting.freshchat.com/")

        self.driver.find_element_by_css_selector()
