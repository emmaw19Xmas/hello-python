# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 3/5/2022 9:48 AM
# @Function:
from selenium.webdriver.common.by import By

from Litemall.page_objects.base_page import BasePage



class HomePage(BasePage):
    _MENU_PRODUCT_MANAGE =(By.XPATH,"//span[contains(text(), '商品管理')]")
    _MENU_PRODUCT_LAUNCH =(By.XPATH,"//span[contains(text(), '商品上架')]")

    def go_to_product_launch(self):
        self.do_click(*self._MENU_PRODUCT_MANAGE)
        self.do_click(*self._MENU_PRODUCT_LAUNCH)

        from Litemall.page_objects.product_launch_page import ProductLaunchPage
        return ProductLaunchPage(self.driver)