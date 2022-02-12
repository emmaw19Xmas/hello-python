# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/27/2021 11:49 AM
# @Function: Page Level - MianPage
from appium.webdriver.webdriver import WebDriver

from Test_wework.base.base import BasePage
from Test_wework.page.ContactPage import Contact_Page


class MainPage(BasePage):

    def goto_contact(self):
        #点击”通讯录“按钮，进入通讯录页
        contact_page = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
        contact_page.click()

        return Contact_Page(self.driver)