# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/27/2021 11:54 AM
# @Function: Page Level - Edit Member info - basic mode

"""
如果在这里全局导入AddMemberPage, 会出现循环导入报错（circular import）
from Test_wework.page.AddmemberPage import AddMemberPage

这里的解决方法是import locally
"""
from appium.webdriver.webdriver import WebDriver

from Test_wework.base.base import BasePage


class EditMemberPage_basic(BasePage):

    #在简易模式下编辑新成员信息
    def edit_memberinfo(self):
        #输入姓名；电话。。。

        el4 = self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../*[@text='必填']")
        el4.send_keys("李雷")
        print("添加李雷")
        el5 = self.driver.find_element_by_xpath("//*[contains(@text,'手机')]/..//*[@text='必填']")
        el5.send_keys("18634560987")
        print("添加李磊的电话号码")
        el6 = self.driver.find_element_by_xpath("//*[@text='保存']")
        el6.click()
        from Test_wework.page.AddmemberPage import AddMemberPage
        return AddMemberPage(self.driver)

