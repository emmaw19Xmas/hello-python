# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/27/2021 11:51 AM
# @Function: Page Level - Contact Page
from Test_wework.page.AddmemberPage import AddMemberPage


class Contact_Page:
    def add_member(self):
        #点击添加成员，进入到添加成员页

        add_button = self.driver.find_element_by_xpath("//*[@text='添加成员']")
        add_button.click()
        print("点击添加成员")

        return AddMemberPage()