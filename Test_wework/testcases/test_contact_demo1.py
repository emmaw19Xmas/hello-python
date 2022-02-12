# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/27/2021 12:02 PM
# @Function: testcase 1
from Test_wework.base.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        pass

    def test_addcontact(self):
        return self.main.goto_contact().add_member().\
            click_addmemebr_manually().\
            edit_memberinfo().\
            back_to_contactpage()

    def test_verify(self):
        while True:
            if "李磊" in self.test_addcontact().page_source:
                print("正在验证")
                break