# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 3/5/2022 9:49 AM
# @Function:
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from Litemall.page_objects.base_page import BasePage


class ProductListPage(BasePage):
    _TEXT_PRODUCT_NAME = (By.XPATH,"//tbody/tr[1]/td[3]/div")

    def get_product_name(self):
        wait = WebDriverWait(self.driver,10)
        element = wait.until(EC.visibility_of_element_located(self._TEXT_PRODUCT_NAME))
        return element.text