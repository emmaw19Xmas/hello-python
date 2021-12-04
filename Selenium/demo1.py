# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/3/2021 7:52 PM
# @Function:
import selenium

from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.google.cn/chrome/")

test_selenium()