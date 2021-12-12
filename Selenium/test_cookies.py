# -*- coding: utf-8 -*-
# @Author  : 18635
# @Time    : 12/11/2021 9:58 PM
# @Function:
from time import sleep

import yaml

from Selenium.base import Base


class TestCookieLogin(Base):
    def test_get_cookies(self):
        self.driver.get("https://ezrouting.freshworks.com/login?")
        sleep(30)
        #get cookie 之前一定要先登录好
        cookies = self.driver.get_cookies()
        # return(cookies)
        # print(cookies)
        with open("cookie.yaml",'w') as f:
            yaml.safe_dump(cookies,f)
    def test_add_cookies(self):
        self.driver.get("https://ezrouting.freshworks.com/login?")
        cookies = yaml.safe_load(open('cookie.yaml'))
        for c in cookies:
            self.driver.add_cookie(c)
        sleep(3)
        self.driver.get("https://ezrouting.freshworks.com/login?")

