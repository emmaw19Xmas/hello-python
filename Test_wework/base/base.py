# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/27/2021 4:37 PM
# @Function: base page for the program
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    """
    还可以封装常见方法
    """
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_click(self, by, locator):
        self.find(by,locator).click()

    def find_sendkeys(self, by, locator, text):
        self.find(by, locator).send_keys(text)