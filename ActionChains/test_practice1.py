# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/6/2021 8:43 PM
# @Function:
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class test_ActionChain():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("xxxxx")
        ele_click = self.driver.find_element_by_id("xxx")
        ele_2click = self.driver.find_element_by_xpath("xxx")
        ele_rightclick = self.driver.find_element_by_id("xxx")

        action = ActionChains(self.driver)
        action.click(ele_click)
        action.context_click(ele_rightclick)
        action.double_click(ele_2click)
        sleep(3)
        action.perform()
        sleep(3)

    def test_moveto_element(self):
        self.driver.get("xxxx")
        ele = self.driver.find_element_by_link_text("xxx")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    def test_drag_and_drop(self):
        self.driver.get("xxx")
        ele_drag = self.driver.find_element_by_id("xxx")
        ele_drop = self.driver.find_element_by_id("xxx")
        action = ActionChains(self.driver)
        #1
        action.drag_and_drop(ele_drag, ele_drop).perform()
        #2
        action.click_and_hold(ele_drag).release(ele_drop).perform()
        #3
        action.click_and_hold(ele_drag).move_to_element(ele_drop).release().perform()
        sleep(3)

    def test_keys(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.BACK_SPACE)
        action.key_down(Keys.CONTROL).send_keys('a').keyp_up(Keys.CONTROL)
        action.perform()