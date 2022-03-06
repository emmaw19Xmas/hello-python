# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 3/5/2022 9:49 AM
# @Function:
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

#_BASE_URL = 'http://litemall.hogwarts.ceshiren.com/#/login?redirect=%2Fdashboard'

class BasePage:
    _BASE_URL = 'http://litemall.hogwarts.ceshiren.com'
    def __init__(self,driver:WebDriver =None):
        if driver is None:
            #初始化浏览器
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()
            self.driver.get(self._BASE_URL)

        else:
            self.driver = driver

    def do_click(self, by:By, locator:str):
        self.driver.find_element(by, locator).click()

    def do_send_keys(self, value:str, by:By, locator:str):
        element = self.driver.find_element(by, locator)
        element.clear() #避免已有内容的干扰
        element.send_keys(value)

    # def do_scroll_to_bottom(self):
    #     self.driver.execute_script('Window.scrollTo(0,document.body.scrollHeight)')
    # def find_element(self,by:By, locator:str):
    #     self.driver.find_element(by, locator)

