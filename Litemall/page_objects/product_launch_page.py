# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 3/5/2022 9:48 AM
# @Function:
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Litemall.page_objects.base_page import BasePage



class ProductLaunchPage(BasePage):
    _INPUT_PRODUCE_CODE = (By.XPATH,"//label[@for='goodsSn']/../div/div/input")
    _INPUT_PRODUCE_NAME = (By.XPATH,"//label[@for='name']/../div/div/input")
    _INPUT_PRODUCE_PRICE = (By.XPATH,"//label[@for='counterPrice']/../div/div/input")
    _RADIO_HOT = (By.XPATH,"//span[contains(text(),'热卖')]")
    _BUTTON_LAUNCH = (By.XPATH,"//button/span[contains(text(), '上架')]/..")

    def product_launch(self):
        #输入商品编号
        self.do_send_keys('1234',*self._INPUT_PRODUCE_CODE)
        #输入商品名称
        self.do_send_keys('1234',*self._INPUT_PRODUCE_NAME)
        #输入市场售价
        self.do_send_keys('1234',*self._INPUT_PRODUCE_PRICE)
        #点击热卖按钮
        self.do_click(*self._RADIO_HOT)
        #滑到页面底部
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        #点击上架按钮
        self.do_click(*self._BUTTON_LAUNCH)
        from Litemall.page_objects.product_list_page import ProductListPage
        return ProductListPage(self.driver)
