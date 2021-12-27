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
        self.main.goto_contact().add_member().\
            click_addmemebr_manually().edit_memberinfo()
        ###12：39 pm 现在的问题是如何backto contact list
        while True:
            if "韩梅梅" in self.driver.page_source:
                # print(self.driver.page_source)
                break