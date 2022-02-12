# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/27/2021 11:51 AM
# @Function: Page Level - Contact Page
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from Test_wework.base.base import BasePage
from Test_wework.page.AddmemberPage import AddMemberPage


class Contact_Page(BasePage):
    add_member_button = (MobileBy.XPATH, "//*[@text='添加成员']")

    def add_member(self):
        #点击添加成员，进入到添加成员页
        #以下两行注释为阶段2的代码
        # add_button = self.driver.find_element_by_xpath("//*[@text='添加成员'")
        # add_button.click()
        #下面这一行是阶段3的代码
        self.find_click(*self.add_member_button)
        print("点击添加成员")

        return AddMemberPage(self.driver)