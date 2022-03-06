# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 3/5/2022 9:48 AM
# @Function:
from selenium.webdriver.common.by import By

from Litemall.page_objects.base_page import BasePage



class LoginPage(BasePage):
    _INPUT_USERNAME = (By.XPATH,"//input[@name='username']")
    _INPUT_PASSWORD = (By.XPATH,"//input[@name='password']")
    _BUTTON_LOGIN =(By.CSS_SELECTOR,"button.el-button")

    def login(self):
        #输入用户名，密码，然后登录
        self.do_send_keys("admin123", *self._INPUT_USERNAME)
        self.do_send_keys("admin123", *self._INPUT_PASSWORD)
        self.do_click(*self._BUTTON_LOGIN)
        from Litemall.page_objects.home_page import HomePage
        return HomePage(self.driver)