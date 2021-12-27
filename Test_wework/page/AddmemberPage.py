# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/27/2021 11:52 AM
# @Function: Page Level - Add Member Page
from Test_wework.page.EditMemberPage_basic import EditMemberPage_basic


class AddMemberPage:
    def click_addmemebr_manually(self):
        #点击，进入手动添加成员页
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[3]/android.widget.LinearLayout/android.widget.TextView")
        el3.click()
        return EditMemberPage_basic()